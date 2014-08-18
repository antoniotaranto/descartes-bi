from __future__ import unicode_literals

from django.contrib import admin

from .admin_forms import DatasourceForm
from .models import Datasource, Host


class DatasourceAdmin(admin.ModelAdmin):
    form = DatasourceForm
    list_display = ('label', 'host', 'data_format', 'python_enabled')
    list_editable = ('host',)


class HostAdmin(admin.ModelAdmin):
    list_display = ('label', 'netloc')
    list_editable = ('netloc',)


admin.site.register(Datasource, DatasourceAdmin)
admin.site.register(Host, HostAdmin)
