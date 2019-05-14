from django.db import models

# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)