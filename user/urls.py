from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = 'user'

urlpatterns = [
    path('register/', views.Register, name="register"),
    path('profile/', views.Profile, name="profile"),
    path('profile_update/', views.ProfileUpdate, name="profile_update"),
    path('login/', auth_view.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name="user/logout.html"), name='logout'),


]