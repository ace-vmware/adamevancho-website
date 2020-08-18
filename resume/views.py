from django.shortcuts import render
from .models import DarkMode
from django.http import HttpResponse

# Create your views here.
def home(request):
    switch = {
        'DarkMode': DarkMode.objects.all()[0],
        'LightMode': DarkMode.objects.all()[1]
    }
    return render(request, 'resume/index.html', switch)

def homeDark(request):
    return render(request, 'resume/index_dark.html')