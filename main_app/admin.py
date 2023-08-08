from django.contrib import admin
from .models import Event, Vendor, Rating
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Event)
admin.site.register(Rating)