from django import forms


class FileUpload(forms.Form):
    file = forms.FileField()
