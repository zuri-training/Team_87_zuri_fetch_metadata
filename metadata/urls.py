from imp import get_magic
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


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
    path("save", views.save, name="save"),
    path("review/<int:pk>", views.review, name="review"),
    path("history/<int:pk>", views.history.as_view(), name="history"),
    path("change_email/<int:pk>", views.change_email.as_view(), name="change_email"),
    path("update_picture", views.accountSettings, name='update_picture'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
