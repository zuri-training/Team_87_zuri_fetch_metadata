from django.contrib import admin
from .models import Contact, Profile, History, Files

# Register your models here.
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(History)
admin.site.register(Files)
