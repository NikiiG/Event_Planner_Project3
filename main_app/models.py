from django.db import models

# Create your models here.
class event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)