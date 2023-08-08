from django.db import models
from datetime import date

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
    Category = models.CharField(
    max_length=1,
    choices=CAT,
    default=CAT[0][0]
  )
    vendors = models.ManyToManyField(Vendor)
    participants = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.id}'


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