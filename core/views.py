from django.http import HttpResponse
from django.shortcuts import render
from .models import Project
from .forms import RegistrationForm

def home(request):
    return HttpResponse("Team Formation Platform")

def projects(request):
    projects = Project.objects.all()
    return render(request, "core/projects.html", {"projects": projects})

def register(request):
    form = RegistrationForm()
    return render(request, "core/register.html", {"form": form})
