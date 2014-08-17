from django.contrib import admin

from .models import (ChartJSBarWidget, ChartJSLineWidget, JustgageWidget,
                     MessageWidget, NovusLineChartWidget, WebsiteWidget)

admin.site.register(ChartJSBarWidget)
admin.site.register(ChartJSLineWidget)
admin.site.register(JustgageWidget)
admin.site.register(MessageWidget)
admin.site.register(NovusLineChartWidget)
admin.site.register(WebsiteWidget)
