from django.shortcuts import render
from django.views import generic
from .models import Ocrimage
# Create your views here.

class OcrimageList(generic.ListView):
    queryset = Ocrimage.objects.filter(status=1).order_by('-created_on')
    template_name = 'ocr/index.html'