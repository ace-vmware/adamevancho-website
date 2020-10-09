from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.home, name='resume-home'),
    path('dark', views.homeDark, name='resume-dark'),
    path('responsivepage1', views.responsivePage1, name='resume-responsivepage1'),
    path('responsivepage2', views.responsivePage2, name='resume-responsivepage2'),
    path('responsivepage3', views.responsivePage3, name='resume-responsivepage3')
    ]