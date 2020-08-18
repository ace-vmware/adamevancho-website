# api/resources.py
from tastypie.resources import ModelResource
from .models import DarkMode
from tastypie.authorization import Authorization

class DarkModeResource(ModelResource):
    class Meta:
        queryset = DarkMode.objects.all()
        resource_name = 'DarkMode'
        authorization = Authorization()