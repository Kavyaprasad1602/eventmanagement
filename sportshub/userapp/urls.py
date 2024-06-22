# urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('', views.user, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
