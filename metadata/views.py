import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
import os

from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.encoding import smart_str
from metadata.models import Contact, History, Files
from django.http import HttpResponseRedirect
from .forms import FileUpload, ProfileForm


# import helper function defined in helper_functions.py
from .helperFuncs.extractImage import extract_image_metadata
# from helperFuncs.pillow import extract_image_metadata_with_pillow

# ================
# import packages for extracting metadata
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from tinytag import TinyTag

# ================
# import for csv
import csv

# Create your views here.

#=========
# import jsson to save the results
import json
#===

def index(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        context = {'username': username}
    return render(request, "index.html", context)


# ==============================================
# =============================================


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid email or password')
            return redirect('metadata:login')
    return render(request, "login.html")


# ============================================
# ============================================


def logout(request):
    auth.logout(request)
    return redirect('/')


# =============================================
# =============================================


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        pass2 = request.POST['pass2']
        email = email.lower()
        if password == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('metadata:signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect('metadata:signup')
            else:
                user = User.objects.create_user(
                    username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                messages.info(request, "Account created")
                return HttpResponseRedirect("login")
        else:
            messages.info(request, "Password didnt match")
            return redirect('metadata:signup')

    return render(request, "signup.html")


class profile(LoginRequiredMixin, View):
    login_url = '/login'
    success_url = reverse_lazy('metadata:profile')
    model = User
    template_name = 'profile.html'

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, self.template_name)

    def post(self, request, pk):
        if request.POST['type'] == '1':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            User.objects.filter(id=pk).update(
                first_name=first_name, last_name=last_name)
            messages.info(request, "Update Succcessful")
            return redirect('metadata:profile', pk=pk)
        else:
            username = request.POST['username']
            password1 = request.POST['pass1']
            password2 = request.POST['pass2']
            if password1 == password2:
                u = User.objects.get(username=username)
                u.set_password(password1)
                u.save()
                messages.info(request, "Password updated!!")
                user = auth.authenticate(username=username, password=password1)
                if user is not None:
                    auth.login(request, user)
                    return redirect('metadata:profile', pk=pk)

            else:
                messages.info(request, "Password did not match!!")
                return redirect('metadata:profile', pk=pk)


def handle_uploaded_file(f):
    with open('metadata / upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# ===========================================
# ==========================================

def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
        contact.save()
        messages.info(request, "Message sent")
        return redirect('metadata:contact')
    return render(request, "contact.html")

# ==========================================
# ==========================================


class view_metadata(LoginRequiredMixin, View):
    success_url = reverse_lazy('metadata:viewMetadata')
    template_name = 'metadata.html'
    login_url = '/login'
    REDIRECT_FIELD_NAME = 'next'

    def post(self, request):
        form = FileUpload(request.POST, request.FILES)
        context = {"metadata": []}

        if form.is_valid():

            uploaded_file = request.FILES['upload_file']
            file_type = uploaded_file.content_type.split("/")

            if file_type[0] == "video" or file_type[0] == "image" or file_type[0] == "audio":

                extracted_metadata = extract_image_metadata(
                    file_type[0], uploaded_file)
                context['metadata'] += extracted_metadata
            #check the file size and  save to  database if less than 20mb
            request.session["metadata"] = context
            a = request.session.get("metadata")
            size  = a['metadata'][1]['tag_value']
            if int(size) > 20000000:
                name = a['metadata'][0]['tag_value']
                owner = request.user
                data = Files(file_name=name,
                             uploaded_file=uploaded_file, owner=owner)
                data.save()
                
            

            return redirect("metadata:result")
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = FileUpload()
        return render(request, self.template_name, {'form': form})

# ================================================
# ================================================


def result(request):
    metadata = request.session.get("metadata")
    context = metadata
    return render(request, "result.html", context)


# ============================================
# ============================================
def save(request):
    metadata = request.session.get("metadata")
    name = metadata['metadata'][0]['tag_value']
    owner = request.user
    #size = metadata['metadata'][1]['tag_value']
    if History.objects.filter(name=name).exists() and History.objects.get(name=name).owner == owner:
        messages.info(request, "Data already present in your save history")
        return render(request, "index.html")
    else:
        data = json.dumps(metadata)
        history = History(data=data, name=name, owner=owner)
        history.save()
        messages.info(request, "data saved succesfully")
        return render(request, "index.html")

##================


class saved_files(LoginRequiredMixin, View):
    login_url = '/login'
    model = Files
    template_name = 'saved_files.html'
    def get(set,request):
        owner = request.user
        files = Files.objects.all()
        context = {"owner": owner, "files": files}
        return render(request, "saved_files.html", context)


##=====

def review(request, pk):
    data= History.objects.get(id=pk)
    metadata = json.loads(data.data)
    context = metadata
    request.session["metadata"] = context
    return render(request, "result.html", context)




#===============


class history(LoginRequiredMixin, View):
    login_url = '/login'
    success_url = reverse_lazy('metadata:history')
    model = History
    template_name = 'saved.html'

    def get(self, request, pk):
        user = request.user
        history = History.objects.all()
        # print(history)
        # user = request.user
        # no = 1
        # for i in history:
        #      if i.owner == user:
        #         user_history[no] = {"name":i.name,"data":i.data,"time":i.created_at}
        #         no +=1
        # print(user_history)
                
        context = {"history":history,"user":user}
        return render(request, self.template_name, context)

        


#==============

def download_csv_data(request):
    # response content type
    metadata = request.session.get("metadata")
    metadata_label = list(metadata.keys())[1:]

    response = HttpResponse(content_type='text/csv')
    # decide the file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.csv"'

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    # writer.writerow(metadata_label)

    metadata_label_name = []
    metadata_label_value = []

    for metadata_val in metadata["metadata"]:
        metadata_label_name.append(smart_str(metadata_val["label_name"]))
        metadata_label_value.append(smart_str(metadata_val["label_value"]))

    writer.writerow(metadata_label_name)
    writer.writerow(metadata_label_value)

    return response


# =================================================
# =================================================

class change_email(LoginRequiredMixin, View):
    success_url = reverse_lazy('metadata:profile')
    template = 'change_email.html'

    def get(self, request, pk):
        return render(request, self.template)

    def post(self, request, pk):
        email = request.POST['new_email']
        email = email.lower()
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist choose another one")
            return redirect('metadata:change_email', pk=pk)
        else:
            User.objects.filter(id=pk).update(email=email)
            messages.info(request, "Email succesfully updated")
        return redirect('metadata:profile', pk=pk)


# =====================================================
# =====================================================


def accountSettings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request, "Picture Updated succesfully!")
            return redirect('metadata:index')
    context = {'form': form}
    return render(request, 'update_picture.html', context)
