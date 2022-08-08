from bz2 import compress
from re import M
from stat import FILE_ATTRIBUTE_HIDDEN
from tkinter import N
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            2, "Name must be greater than 2 characters")]
    )
    email = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.message) < 15:
            return self.message
        return self.text[:11] + ' ...'


class Profile(models.Model):
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        # show how we want it to be displayed
        return f'{self.user.username} Profile'


class History(models.Model):
    name = models.CharField(max_length=200)
    #size = models.IntegerField()
    data = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    uploaded_file = models.FileField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class other(models.Model):
    pass
