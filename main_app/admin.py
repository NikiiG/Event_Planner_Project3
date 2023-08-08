from django.contrib import admin
from .models import Vendor, Event, Category, Rating

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Rating)