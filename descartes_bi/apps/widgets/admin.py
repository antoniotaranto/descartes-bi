from django.contrib import admin

from .models import (ChartJSBarWidget, ChartJSDoughnutWidget, ChartJSLineWidget,
                     ChartJSPieWidget, ChartJSRadarWidget, JustgageWidget,
                     MessageWidget, NovusLineChartWidget, WebsiteWidget)

admin.site.register(ChartJSBarWidget)
admin.site.register(ChartJSDoughnutWidget)
admin.site.register(ChartJSLineWidget)
admin.site.register(ChartJSPieWidget)
admin.site.register(ChartJSRadarWidget)
admin.site.register(JustgageWidget)
admin.site.register(MessageWidget)
admin.site.register(NovusLineChartWidget)
admin.site.register(WebsiteWidget)
