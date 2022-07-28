from django.contrib import admin
from django.urls import path
from . import views
app_name = 'metadata'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path("profile/<int:pk>", views.profile.as_view(), name="profile"),
    path("contact", views.contact, name="contact"),

]
