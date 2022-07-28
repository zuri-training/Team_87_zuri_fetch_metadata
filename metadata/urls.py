from imp import get_magic
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from . import views
app_name= 'metadata'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path("profile/<int:pk>", views.profile.as_view(), name="profile"),
    
=======
from .views import get_metadata, login, signup, index, profile

urlpatterns = [
    path("", index, name="index"),
    path("login", login, name="login"),
    path("signup", signup, name="signup"),
    path("profile", profile, name="profile"),
    path("metadata", get_metadata, name="metadata")
>>>>>>> 0560008 (added the input for uploading file)
]
