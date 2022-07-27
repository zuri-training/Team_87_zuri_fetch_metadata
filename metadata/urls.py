from django.contrib import admin
from django.urls import path
from .views import login, signup, index, profile

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("signup", signup, name="signup"),
    path("profile", profile, name="profile")
]
