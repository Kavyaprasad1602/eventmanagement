from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('contact/', views.contact, name='contact'),
    path('registration/', views.registration, name='registration'),
    path('events/', views.events, name='events'),
    path('event/', views.signup, name='signup'),
    path('event/', views.login, name='login'),

]
