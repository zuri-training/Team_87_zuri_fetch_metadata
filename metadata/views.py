import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from .forms import FileUpload
from django.http import HttpResponseRedirect
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

# Create your views here.


def index(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        context = {'username': username}
    return render(request, "index.html", context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('/login')
        return render(request, 'login.html')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        if password == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                messages.info(request, "Account created")
                return HttpResponseRedirect("login")
        else:
            messages.info(request, "Password didnt match")
            return redirect('signup')

    return render(request, "signup.html")


class profile(LoginRequiredMixin, View):
    login_url = '/login'
    success_url = reverse_lazy('metadata:profile')
    model = User
    template_name = 'profile.html'

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, self.template_name)


def handle_uploaded_file(f):
    with open('metadata / upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def view_metadata(request):
    if request.method == "POST":
        form = FileUpload(request.POST, request.FILES)
        # print(request.FILES["upload_file"])
        if form.is_valid():
            # handle_uploaded_file(request.FILES["upload_file"])
            print(request.FILES['upload_file'].content_type)
            print(request.FILES['upload_file'].name)
            print(request.FILES['upload_file'].size)
            parser = createParser(request.FILES['upload_file'])
            print(extractMetadata(parser))
            HttpResponseRedirect("/")

    else:
        form = FileUpload()

    return render(request, 'metadata.html', {'form': form})
