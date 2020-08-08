from django.shortcuts import render
from .models import Modal
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'projects': Modal.objects.all()
    }
    return render(request, 'resume/index.html', context)