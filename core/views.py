from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

def home(request):
    return HttpResponse("Team Formation Platform")

def projects(request):
    projects = Project.objects.all()
    return render(request, "core/projects.html", {"projects": projects})