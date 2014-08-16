import logging
import os
import re

from django import http
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext

logger = logging.getLogger(__name__)


def error500(request, template_name='500.html'):
    # TODO: if user is admin include debug info
    t = loader.get_template(template_name)

    return http.HttpResponseServerError(t.render(RequestContext(request, {
        'project_name': settings.PROJECT_TITLE})))


def set_language(request):
    if request.method == 'GET':
        request.session['django_language'] = request.GET.get('language', 'en')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    return render_to_response('home.html', {},
        context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', {},
        context_instance=RequestContext(request))


def get_project_root():
    """
    Get the project root directory
    """
    settings_mod = __import__(settings.SETTINGS_MODULE, {}, {}, [''])
    return os.path.dirname(os.path.abspath(settings_mod.__file__))
