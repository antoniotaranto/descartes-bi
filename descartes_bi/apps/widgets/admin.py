from django.contrib import admin

from .models import MessageWidget, WebsiteWidget

admin.site.register(MessageWidget)
admin.site.register(WebsiteWidget)
