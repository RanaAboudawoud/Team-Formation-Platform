from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Project, Profile, Collaborator_profile, Collaborator_skill, Idea_maker_profile
from .forms import RegistrationForm, CollaboratorForm, LoginForm, IdeaMakerForm
from .matching import rank_projects

def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        collaborator = Collaborator_profile.objects.get(profile__user = request.user)
    except Collaborator_profile.DoesNotExist:
        return redirect("collaborator_profile")

    ranked_projects = rank_projects(collaborator)

    return render(request, "core/home.html", {"ranked_projects": ranked_projects})


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

            return redirect("login")
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
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = CollaboratorForm(request.POST)
        if form.is_valid():
            skill = form.cleaned_data["skill"]
            proficiency = form.cleaned_data["proficiency"]
            availability = form.cleaned_data["availability"]

            user = request.user

            #Spara information från användare i respektive databas
            profile = Profile.objects.get(user = user)
            collaborator, created = Collaborator_profile.objects.update_or_create(profile = profile, defaults = {"availability": availability})
            Collaborator_skill.objects.update_or_create(collaborator = collaborator, skill = skill, defaults = {"proficiency": proficiency})

            return redirect("home")
    else:
        form = CollaboratorForm()

    return render(request, "core/collaborator_profile.html", {"collaborator_form": form})

def idea_maker_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    user = request.user
    profile = Profile.objects.get(user = user)
    idea_maker, created = Idea_maker_profile.objects.get_or_create(profile = profile)

    if request.method == "POST":
        form = IdeaMakerForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data["bio"]

            idea_maker.bio = bio
            idea_maker.save()

            return redirect("idea_maker_profile")
    else:
        form = IdeaMakerForm(initial = {"bio": idea_maker.bio})

    return render(request, "core/idea_maker_profile.html", {"idea_maker_form": form, "idea_maker": idea_maker})