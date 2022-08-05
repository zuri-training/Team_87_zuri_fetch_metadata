from bz2 import compress
from re import M
from stat import FILE_ATTRIBUTE_HIDDEN
from tkinter import N
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
    # Delete profile when user is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        # show how we want it to be displayed
        return f'{self.user.username} Profile'


class ImageMetadata(models.Model):
    filename = models.CharField(max_length=250)
    filesize = models.CharField(max_length=20)
    filetype = models.CharField(max_length=20)
    mimetype = models.CharField(max_length=50)
    imagewidth = models.CharField(max_length=120, null=True)
    imagelength = models.CharField(max_length=120, null=True)
    imageorientation = models.CharField(max_length=120, null=True)
    bitspixel = models.CharField(max_length=120, null=True)
    pixelformat = models.CharField(max_length=120, null=True)
    creationdate = models.CharField(max_length=120, null=True)
    cameraaperture = models.CharField(max_length=120, null=True)
    camerafocal = models.CharField(max_length=50, null=True)
    cameraexposure = models.CharField(max_length=50, null=True)
    cameramodel = models.CharField(max_length=120, null=True)
    cameramanufacturer = models.CharField(max_length=120, null=True)
    compression = models.CharField(max_length=120, null=True)
    isospeed = models.CharField(max_length=50, null=True)
    exifversion = models.CharField(max_length=50, null=True)
    shutterspeed = models.CharField(max_length=50, null=True)
    aperture = models.CharField(max_length=50, null=True)
    exposure_bias = models.CharField(max_length=120, null=True)
    focallength = models.CharField(max_length=50, null=True)
    producer = models.CharField(max_length=120, null=True)
    comment = models.CharField(max_length=120, null=True)
    formatversion = models.CharField(max_length=120, null=True)
    resolutionunit = models.IntegerField(null=True)
    exifoffset = models.IntegerField(null=True)
    make = models.CharField(max_length=120, null=True)
    model = models.CharField(max_length=120, null=True)
    software = models.CharField(max_length=120, null=True)
    orientation = models.IntegerField(null=True)
    datetime = models.CharField(max_length=120, null=True)
