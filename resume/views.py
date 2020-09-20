from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    }
    return render(request, 'resume/index.html', context)

def homeDark(request):
    return render(request, 'resume/index_dark.html')

def responsivePage1(request):
    return render(request, 'responsivepage1/index.html')

def responsivePage2(request):
    return render(request, 'responsivepage2/index.html')