from django.db import models

# Create your models here.
class Modal(models.Model):
    description = models.TextField()
    projectName = models.CharField(max_length=100, default='unnamed project')

    def __str__(self):
        return self.projectName

class DarkMode(models.Model):
    currentMode = models.CharField(max_length=5)
    path = models.CharField(max_length=20)
    is_on = models.BooleanField()

    def __str__(self):
        return self.currentMode