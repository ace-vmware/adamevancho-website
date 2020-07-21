from django.urls import path
from . import views

# This urls.py comes second.
# At this point: http://www.website.com/sfdcTools/ has already been reached.
# '' will return a page with nothing after http://.../sfdcTools/
urlpatterns = [
    path('', views.sfdcTools, name='sfdcTools-home'),
    path('about/', views.sfdcTools, name='sfdcTools-about')]