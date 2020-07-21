from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sfdcTools(request):
    # return HttpResponse("<h1>sfdcTools Page</h1>")
    return render(request, 'sfdcTools/base.html')

def sfdcToolsAbout(request):
    return render(request, 'sfdcTools/about.html')