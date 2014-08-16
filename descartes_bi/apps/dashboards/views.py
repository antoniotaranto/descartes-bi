import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Dashboard

logger = logging.getLogger(__name__)

# TODO: login required

class DashboardListView(ListView):
    model = Dashboard
