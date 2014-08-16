from __future__ import absolute_import

from django.conf.urls import patterns, url

from .views import DashboardListView

urlpatterns = patterns('',
    url(r'^$', DashboardListView.as_view(), name='dashboard_list'),
    #url(r'^(?P<pk>\d+)/$', dashboard_view, (), 'dashboard_view'),
)
