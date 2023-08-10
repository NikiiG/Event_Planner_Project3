from django.urls import reverse
from django.core.paginator import Paginator
from urllib import request
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
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
    context = {'event': event}
    comments = Comment.objects.filter(event=event)

    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save(commit = False)
            comment.user = request.user
            comment.event = event
            comment.save()

        else:
            form = CommentForm()
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
def dashboard(request):
        user_vendors = Vendor.objects.all()
        user_events = Event.objects.all()

        context = {
            'user_events': user_events,
            'user_vendors': user_vendors,
        }
        return render(request, 'dashboard.html', context)

def contact_list(request):
    return render(request, 'contact_list.html')

