from django.urls import reverse
from django.core.paginator import Paginator
from urllib import request
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm
from .models import Event, Category, Vendor, Rating, Comment
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
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
    fields = ['name', 'date', 'location', 'description', 'category', 'participants', 'vendors']

    def form_valid(self, form):
        # self.request.user is the logged in user
        form.instance.user = self.request.user
        # Let the CreateView's form_valid method
        # do its regular work (saving the object & redirecting)
        return super().form_valid(form)


def upcoming_events(request):
    upcoming_events = Event.objects.order_by('date')
    context = {'upcoming_events': upcoming_events}
    return render(request, 'upcoming_events.html', context)

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    related_vendors = event.vendors.all()
    available_vendors = Vendor.objects.exclude(event=event) 
    comments = Comment.objects.filter(event=event) 
    context = {
        'event': event,
        'related_vendors': related_vendors,
        'available_vendors': available_vendors,
        'comments': comments,
    }
    return render(request, 'events/event_detail.html', context)



class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name', 'date', 'location', 'description', 'category', 'participants', 'vendors']


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = "/upcoming_events"

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('upcoming_events')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def contact_list(request):
    return render(request, 'contact_us.html')


@login_required
def dashboard(request):
    user_vendors = Vendor.objects.all()
    user_events = Event.objects.filter(user_id=request.user)    

    context = {
        'user_events': user_events,
        'user_vendors': user_vendors,
    }
    return render(request, 'dashboard.html', context)


class comment_create(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_create.html'

    def form_valid(self, form):
        event_id = self.kwargs['event_id']
        event = get_object_or_404(Event, id=event_id)

        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.event = event
        comment.save()

        return redirect('event_detail', event_id=event_id)

@login_required
def assoc_vendor(request, event_id, vendor_id):
    event = Event.objects.get(id=event_id)
    vendor = Vendor.objects.get(id=vendor_id)
    event.vendors.add(vendor)
    return redirect('event_detail', event_id=event_id)

@login_required
def unassoc_vendor(request, event_id, vendor_id):
    event = Event.objects.get(id=event_id)
    vendor = Vendor.objects.get(id=vendor_id)
    event.vendors.remove(vendor)
    return redirect('event_detail', event_id=event_id)

