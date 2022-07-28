from django.contrib import admin
from django.urls import path
from . import views
from .models import ProfilePage

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path("old_profile", views.profile, name="show_profile"),
    path("profile/<int:pk>", ProfilePage.as_view(), name="profile"),
    
]
