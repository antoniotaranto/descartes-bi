from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .literals import DEFAULT_ELEMENT_HEIGHT
from .managers import DashboardElementManager

from widgets.models import WidgetBase


@python_2_unicode_compatible
class Dashboard(models.Model):
    label = models.CharField(max_length=96, verbose_name=_('Label'))

    def __str__(self):
        return self.label

    def get_element_rows(self):
        rows = []
        row = []
        spans = 0
        for element in self.active_elements():
            spans += element.span
            if spans > 12:
                rows.append(row)
                spans = element.span
                row = []

            row.append(element)

        if row:
            rows.append(row)

        return rows

    class Meta:
        verbose_name = _('Dashboard')
        verbose_name_plural = _('Dashboards')


class DashboardElement(models.Model):
    dashboard = models.ForeignKey(Dashboard, verbose_name=_('Dashboard'), related_name='elements')
    enabled = models.BooleanField(default=True, verbose_name=_('Enabled'))
    span = models.PositiveIntegerField(help_text=_('The amount of columns in a 12 columns layout that this element should occupy.'), verbose_name=_('Span'))
    height = models.PositiveIntegerField(default=DEFAULT_ELEMENT_HEIGHT, verbose_name=_('Height'))
    order = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name=_('Order'))
    widget = models.ForeignKey(WidgetBase, verbose_name=_('Widget'))

    objects = DashboardElementManager()

    class Meta:
        verbose_name = _('Dashboard element')
        verbose_name_plural = _('Dashboard elements')
