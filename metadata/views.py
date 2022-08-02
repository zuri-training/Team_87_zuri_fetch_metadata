import json
from django.http import HttpResponse
from django.utils.encoding import smart_str
from metadata.models import Contact
from django.http import HttpResponseRedirect
from .forms import FileUpload
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect, get_object_or_404

# =================
# import helper function defined in helper_functions.py
from .helperFuncs.pillow import extract_image_metadata_with_pillow
from .helperFuncs.hachoir import extract_metadata_with_hachoir
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
                return redirect("metadata:login")
        else:
            messages.info(request, "Password didnt match")
            return redirect('metadata:signup')

    return render(request, "signup.html")


# ============================================
# ============================================


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

            # context["metadata"].append(
            #     {"tag_name": "File name", "tag_value": uploaded_file.name.capitalize()})
            # context["metadata"].append(
            #     {"tag_name": "File size", "tag_value": uploaded_file.size})
            # context["metadata"].append(
            #     {"tag_name": "File type", "tag_value": file_type[1].capitalize()})
            # context["metadata"].append(
            #     {"tag_name": "Mime type", "tag_value": uploaded_file.content_type.capitalize()})

            if file_type[0] == "video" or file_type[0] == "image" or file_type[0] == "audio":

                extracted_metadata = extract_image_metadata(
                    file_type[0], uploaded_file)
                context['metadata'] += extracted_metadata

            request.session["metadata"] = context
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


class change_email(LoginRequiredMixin, View):
    success_url = reverse_lazy('metadata:profile')
    template = 'change_email.html'

    def get(self, request, pk):
        return render(request, self.template)

    def post(self, request, pk):
        email = request.POST['new_email']
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exist choose another one")
            return redirect('metadata:change_email', pk=pk)
        else:
            User.objects.filter(id=pk).update(email=email)
            messages.info(request, "Email succesfully updated")
        return redirect('metadata:profile', pk=pk)
