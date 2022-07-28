from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
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
        password2 = request.POST['pass2']
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
                return redirect('login')
        else:
            messages.info(request, "Password didnt match")
            return redirect('signup')

    return render(request, "signup.html")


def profile(request):
    return render(request, "profile.html")
