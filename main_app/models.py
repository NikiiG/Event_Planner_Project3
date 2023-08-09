from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
CAT = (
    ('B', 'Bootcamp'),
    ('S', 'Social Event')
)

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    pricing = models.CharField()
    def __str__(self):
        return f'{self.name}, {self.id}'


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
    max_length=1,
    choices=CAT,
    default=CAT[0][0]
    
  )
    # vendors = models.ManyToManyField(Vendor)
    participants = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.id}'
    def get_absolute_url(self):
        return reverse('home') 

class Category(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()
    age_group = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}, {self.id}'



class Rating(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value}, star'