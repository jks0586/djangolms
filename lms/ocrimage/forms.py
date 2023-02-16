from django import forms
from .models import Ocrimage
class ImageUpload(forms.ModelForm):
    class Meta:
        model = Ocrimage
        fields = ['title','slug','image']