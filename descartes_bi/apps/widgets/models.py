from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from model_utils.managers import InheritanceManager

from datasources.models import Datasource


@python_2_unicode_compatible
class WidgetBase(models.Model):
    label = models.CharField(max_length=128, verbose_name=_('Label'))
    datasource = models.OneToOneField(Datasource, null=True, blank=True, verbose_name=_('Datasource'))

    objects = InheritanceManager()

    def __str__(self):
        subclass = WidgetBase.objects.get_subclass(pk=self.pk)
        return '%s (%s)' % (subclass.label, subclass.widget_type)

    def fetch_data(self):
        return self.datasource.get()

    def get_context(self):
        raise NotImplemented

    class Meta:
        ordering = ('label',)


class WebsiteWidget(WidgetBase):
    template_name = 'widgets/website/base.html'
    widget_type = _('Website')

    load_content = models.BooleanField(default=False, verbose_name=_('Load content'), help_text=_('The widget will load the content of the website as pass it as a base64 encoded string to the iframe, relative asset path will not work.'))

    def get_context(self):
        context = {
            'content': self.fetch_data().content.encode('base64'),
            'url': self.datasource.get_full_url(),
            'load_content': self.load_content,
        }
        return context


class MessageWidget(WidgetBase):
    template_name = 'widgets/message/base.html'
    widget_type = _('Message')

    message = models.TextField(verbose_name=_('Message'))

    def get_context(self):
        context = {
            'message': self.message,
        }
        return context

