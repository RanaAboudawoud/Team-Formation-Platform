from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Project, Profile
from .forms import RegistrationForm

def home(request):
    return HttpResponse("Team Formation Platform")

def projects(request):
    projects = Project.objects.all()
    return render(request, "core/projects.html", {"projects": projects})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]

            user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
            Profile.objects.create(user = user, phone_number = phone_number, role = role)

            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "core/register.html", {"form": form})
