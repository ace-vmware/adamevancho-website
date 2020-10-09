from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/base.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def test(request):
    return HttpResponse("<h1>Test Page. It seems to work!</h1>")
    # return render(request, 'blog/about.html', {'title': 'About'})