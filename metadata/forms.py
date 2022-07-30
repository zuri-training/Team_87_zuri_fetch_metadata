from django import forms
from django.contrib.auth.models import User


class FileUpload(forms.Form):
    upload_file = forms.FileField()

