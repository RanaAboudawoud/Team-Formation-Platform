from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Project, Profile
from .forms import RegistrationForm, CollaboratorForm, LoginForm

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

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password =  form.cleaned_data["password"]

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)

                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "core/login.html", {"login_form": form})

def collaborator_profile(request):
    form = CollaboratorForm()

    return render(request, "core/collaborator_profile.html", {"collaborator_form": form})