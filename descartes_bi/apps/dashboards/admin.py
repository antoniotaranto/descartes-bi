from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from suit.admin import SortableModelAdmin, SortableStackedInline

from .admin_forms import DashboardForm
from .models import Dashboard, DashboardElement


class DashboardElementInline(SortableStackedInline):
    extra = 0
    model = DashboardElement
    suit_classes = 'suit-tab suit-tab-elements'
    sortable = 'order'


class DashboardAdmin(SortableModelAdmin):
    form = DashboardForm
    inlines = [DashboardElementInline]
    list_display = ('label', 'description', 'enabled', 'full_screen', 'order')
    list_editable = ('enabled', 'full_screen',)
    sortable = 'order'
    suit_form_tabs = (('configuration', _('Configuration')), ('elements', _('Elements')))

    fieldsets = (
        (_('Basic information'), {
            'classes': ('suit-tab suit-tab-configuration',),
            'fields': ('label', 'description', 'full_screen')
        }),
    )

admin.site.register(Dashboard, DashboardAdmin)
