from django.contrib import admin

from .models import Vendor, Event, Category, Rating, Comment

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Event)
admin.site.register(Rating)
admin.site.register(Comment)