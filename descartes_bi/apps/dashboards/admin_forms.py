from __future__ import unicode_literals

from django import forms
from django.forms import widgets

from suit.widgets import AutosizedTextarea, EnclosedInput, NumberInput


class DashboardForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': forms.Textarea(attrs={'rows': '5', 'class': 'input-xxlarge'}),
            'label': AutosizedTextarea(attrs={'rows': '1', 'class': 'input-xxlarge'}),
        }
