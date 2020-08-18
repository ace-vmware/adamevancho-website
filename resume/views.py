from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    }
    return render(request, 'resume/index.html', context)

def homeDark(request):
    return render(request, 'resume/index_dark.html')