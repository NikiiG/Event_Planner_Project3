from django.shortcuts import render
from .models import Event, Category, Vendor, Rating

# Create your views here.
# def home(request):
#     return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def events_index(request):
    events = Event.objects.all()
    return render(request,'events/index.html',{'events':events} )


def home(request):
    recent_events = Event.objects.order_by('date')[:2]  # Fetch the two closest events
    context = {'recent_events': recent_events}
    return render(request, 'home.html', context)