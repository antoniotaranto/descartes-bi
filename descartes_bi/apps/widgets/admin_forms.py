from __future__ import unicode_literals

from django import forms
from django.forms import widgets

from suit.widgets import AutosizedTextarea, EnclosedInput, NumberInput


class WidgetForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': forms.Textarea(attrs={'rows': '5', 'class': 'input-xxlarge'}),
            'label': AutosizedTextarea(attrs={'rows': '1', 'class': 'input-xxlarge'}),
            'python_code': AutosizedTextarea(attrs={'rows': '6', 'class': 'input-xxlarge'}),
            'javascript_code': AutosizedTextarea(attrs={'rows': '6', 'class': 'input-xxlarge'}),
        }
