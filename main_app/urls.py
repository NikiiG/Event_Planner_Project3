from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='index'),
    path('become_vendor/', views.become_vendor, name='become_vendor'),
    path('event/create/', views.EventCreate.as_view(), name="create_event"),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),


]
