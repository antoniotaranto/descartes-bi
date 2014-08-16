from __future__ import unicode_literals

from furl import furl
import requests

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Host(models.Model):
    label = models.CharField(verbose_name=_('Label'), max_length=64)
    netloc = models.CharField(verbose_name=_('Network Location Part'), max_length=255, help_text=_('Enter the scheme, username, password, host and port. For example: http://username:password@host:port'))

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('Host')
        verbose_name_plural = _('Hosts')


@python_2_unicode_compatible
class Datasource(models.Model):
    host = models.ForeignKey(Host, verbose_name=_('Host'))
    label = models.CharField(verbose_name=_('Label'), max_length=96)
    path = models.TextField(verbose_name=_('Path'), help_text=_('Enter the URL path, query and fragment. For example: /very-long-url-path/?argument=value&second-argument=value'))

    def __str__(self):
        return self.label

    def get(self):
        return requests.get(self.get_full_url())

    def get_full_url(self):
        f = furl(self.host.netloc)
        f.path = self.path
        f.path.normalize()
        return f.url

    class Meta:
        verbose_name = _('Datasource')
        verbose_name_plural = _('Datasources')
