from django import forms


class FileUpload(forms.Form):
    name = forms.CharField(max_length=80)
    upload_file = forms.FileField()
