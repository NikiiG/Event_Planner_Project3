from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('events/', views.events_index, name='index'),
    path('become_vendor/', views.become_vendor, name='become_vendor'),
    path('event/create/', views.EventCreate.as_view(), name="create_event"),
    #nikita
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='Events_update'),
    path('upcoming_events/', views.upcoming_events, name='upcoming_events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='Events_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/<int:event_id>/assoc_vendor/<int:vendor_id>/', views.assoc_vendor, name='assoc_vendor'),
    path('events/<int:event_id>/unassoc_vendor/<int:vendor_id>/', views.unassoc_vendor, name='unassoc_vendor'),
]
