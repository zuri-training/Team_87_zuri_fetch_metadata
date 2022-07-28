from django.db import models
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from .views import User

# Create your models here.



class ProfilePage(DetailView):
    model = User
    template_name = 'user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = User.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context