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

    def render(self, request):
        raise NotImplemented

    class Meta:
        ordering = ('label',)


class WebsiteWidget(WidgetBase):
    widget_type = _('Website')

    def render(self, request, response):
        context = {
            'widget': self,
            'content': self.fetch_data().content.encode('base64'),
        }

        return render_to_response('widgets/website/base.html', context,
            context_instance=RequestContext(request))


class MessageWidget(WidgetBase):
    widget_type = _('Message')

    message = models.TextField(verbose_name=_('Message'))

    def render(self, request, response):
        context = {
            'widget': self,
            'content': self.message,
        }

        return render_to_response('widgets/message/base.html', context,
            context_instance=RequestContext(request))
