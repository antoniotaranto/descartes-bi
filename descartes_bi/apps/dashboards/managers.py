from django.db import models


class DashboardElementManager(models.Manager):
    def enabled(self):
        return self.queryset.filter(enabled=True)
