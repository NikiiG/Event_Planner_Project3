from django.urls import reverse
from django.core.paginator import Paginator
from urllib import request
from django.http import HttpResponseNotAllowed
<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm
>>>>>>> main
from .models import Event, Category, Vendor, Rating, Comment
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
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

def become_vendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendor_name')
        vendor_description = request.POST.get('vendor_description')
        vendor_phone_number = request.POST.get('vendor_phone_number')
        vendor_email = request.POST.get('vendor_email')
        vendor_pricing = request.POST.get('vendor_pricing')
        selected_events = request.POST.getlist('events')

        vendor = Vendor.objects.create(
            name=vendor_name,
            description=vendor_description,
            phone_number=vendor_phone_number,
            email=vendor_email,
            pricing=vendor_pricing
        )

        return redirect('home')  # Adjust 'home' to the appropriate URL name

    return render(request, 'become_vendor.html')


class EventCreate(CreateView):
    model = Event
<<<<<<< HEAD
    fields = ['name','date','location','description','category','participants','vendors']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
=======
    fields = ['name', 'date', 'location', 'description', 'category', 'participants', 'vendors']

    def form_valid(self, form):
        instance = form.save()

        # Redirect to the 'upcoming_events' view
        return redirect(reverse('upcoming_events'))

def upcoming_events(request):
    upcoming_events = Event.objects.order_by('date')
    context = {'upcoming_events': upcoming_events}
    return render(request, 'upcoming_events.html', context)

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)


class EventUpdate(UpdateView):
    model = Event
    fields = "__all__"


class EventDelete(DeleteView):
    model = Event
    success_url = "/upcoming_events"
