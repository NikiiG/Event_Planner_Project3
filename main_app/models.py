from django.db import models
from datetime import date

# Create your models here.
class event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    catagory = models.ForeignKey('catagory', on_delete=models.CASCADE)
    vendor = models.ManyToManyField('vendor')
    participants = models.IntegerField(max_length=255)

    def __str__(self):
        return f'{self.name}, {self.id}'


class catagory(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()
    age_group = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}, {self.id}'

class vendor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    pricing = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.id}'

class rating(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value}, star'