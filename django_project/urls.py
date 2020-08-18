"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include as incl
from users import views as user_views
from resume.resources import DarkModeResource

# If left blank, localhost:8000 will be directed to path('', views.home, name='blog-home')
# Like so:
# path('', include('blog.urls')),

DarkModeResource = DarkModeResource()

urlpatterns = [
    # Resume URL routes
    path('', include('resume.urls')),
    # Blog URL routes
    path('blog/', include('blog.urls')),
    # Admin URL routes
    path('admin/', admin.site.urls),
    # sfdcTools route
    path('sfdcTools/', include('sfdcTools.urls')),
    # Login Path
    path('register/', user_views.register, name='register'),
    # API Path
    url(r'^resume/', incl(DarkModeResource.urls))
]


