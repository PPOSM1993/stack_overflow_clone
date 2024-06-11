from django.urls import path
from . import views

app_name = 'stack_overflow'

urlpatterns = [
    #path('', views.index),
    path('home/', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
]
