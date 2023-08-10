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
from .forms import CommentForm
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
    fields = ['name','date','location','description','category','participants','vendors']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)

def upcoming_events(request):
    upcoming_events = Event.objects.order_by('date')
    context = {'upcoming_events': upcoming_events}
    return render(request, 'upcoming_events.html', context)

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request, 'events/event_detail.html', context)


class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = ['name','date','location','description','category','participants','vendors']


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


def dashboard(request):
    if request.user.is_authenticated:
        user_vendors = Vendor.objects.filter(email=request.user.email)
        user_events = Event.objects.filter(vendors__in=user_vendors)

        context = {
            'user_events': user_events,
            'user_vendors': user_vendors,
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('login')
    
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    #fields = '__all__'
    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.event_id = self.kwargs[ 'pk' ]  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    success_url = "/upcoming_events"
