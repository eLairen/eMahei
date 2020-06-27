
from django import forms
from .models import Topics

class VideoForm(forms.ModelForm):
    class Meta:
        model= Topics
        fields= ["name", "videos"]