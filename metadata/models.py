from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


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
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics',null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
