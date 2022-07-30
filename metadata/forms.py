from django import forms


class FileUpload(forms.Form):
    upload_file = forms.FileField()
