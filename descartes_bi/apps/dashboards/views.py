import logging

from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView

from .models import Dashboard

logger = logging.getLogger(__name__)


class DashboardListView(ListView):
    context_object_name = 'dashboards'
    queryset = Dashboard.objects.filter(enabled=True)


class DashboardDetailView(DetailView):
    context_object_name = 'dashboard'
    model = Dashboard
