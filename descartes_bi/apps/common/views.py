import logging
import os

from django import http
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader
from django.views.generic import TemplateView

from dashboards.models import Dashboard

logger = logging.getLogger(__name__)


def error500(request, template_name='core/500.html'):
    # TODO: if user is admin include debug info
    t = loader.get_template(template_name)

    return http.HttpResponseServerError(t.render(RequestContext(request, {
        'project_name': settings.PROJECT_TITLE})))


def set_language(request):
    if request.method == 'GET':
        request.session['django_language'] = request.GET.get('language', 'en')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['dashboards'] = Dashboard.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'
