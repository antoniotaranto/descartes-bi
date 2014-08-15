#
#    Copyright (C) 2010  Roberto Rosario
#    This file is part of descartes-bi.
#
#    descartes-bi is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    descartes-bi is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with descartes-bi.  If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

handler500 = 'common.views.error500'
urlpatterns = patterns('',
    (r'^', include('namespaces.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^common/', include('common.urls')),
    (r'^dashboards/', include('dashboards.urls', namespace='dashboards')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^reports/', include('reports.urls', namespace='reports')),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += patterns('',
            url(r'^rosetta/', include('rosetta.urls'), name='rosetta'),
        )
