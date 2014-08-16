from django.contrib import admin

from .models import Datasource, Host

admin.site.register(Datasource)
admin.site.register(Host)
