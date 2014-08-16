from django.contrib import admin

from .models import (JustgageWidget, MessageWidget, NovusLineChartWidget,
                     WebsiteWidget)

admin.site.register(JustgageWidget)
admin.site.register(MessageWidget)
admin.site.register(NovusLineChartWidget)
admin.site.register(WebsiteWidget)
