from imp import get_magic
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
    path("viewMetadata", views.view_metadata.as_view(), name="viewMetadata"),
    path("contact", views.contact, name="contact"),
    path("download", views.download_csv_data, name="download"),
    path("result", views.result, name="result"),
    path("change_email/<int:pk>", views.change_email.as_view(), name="change_email"),
    path("update_picture", views.accountSettings, name='update_picture')

]
