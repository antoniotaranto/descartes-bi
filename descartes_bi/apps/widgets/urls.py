from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import WidgetRenderView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', WidgetRenderView.as_view(), name='widget_render'),
)
