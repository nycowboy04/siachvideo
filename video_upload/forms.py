from django import forms
from django.forms import ModelForm
from .models import Map

class VideoForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Map
        fields = [
            'first_name', 'last_name', 'map_name', 'map_data'
        ]
