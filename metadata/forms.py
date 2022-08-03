from django import forms
<<<<<<< HEAD


class FileUpload(forms.Form):
    name = forms.CharField(max_length=80)
    upload_file = forms.FileField()
=======
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile


class FileUpload(forms.Form):
    upload_file = forms.FileField()

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude= ['user']
>>>>>>> refs/remotes/origin/main
