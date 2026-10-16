from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Project, Profile, Collaborator_profile, Collaborator_skill, Idea_maker_profile, Project_role, Project_skill, Project_interest
from . import forms
from .matching import rank_projects

def home(request):
    if not request.user.is_authenticated:
        return redirect("login")

    return render(request, "core/home.html")

def projects(request):
    projects = Project.objects.all()
    return render(request, "core/projects.html", {"projects": projects})

def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
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
        form = forms.RegistrationForm()

    return render(request, "core/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password =  form.cleaned_data["password"]

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)

                profile = Profile.objects.get(user = user)

                if profile.role == "idea_maker":
                    return redirect("idea_maker_profile")
                else:
                    return redirect("collaborator")
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = forms.LoginForm()

    return render(request, "core/login.html", {"login_form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def collaborator_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    try:
        collaborator = Collaborator_profile.objects.get(profile__user = request.user)
    except Collaborator_profile.DoesNotExist:
        return redirect("collaborator_profile")

    collaborator_skills = Collaborator_skill.objects.filter(collaborator = collaborator)

    sector_choices = dict(Project.CATEGORY_CHOICES)

    sector_interests_display = [
        sector_choices[sector] for sector in collaborator.sector_interests
    ]
    
    ranked_projects = rank_projects(collaborator)

    interests = Project_interest.objects.filter(collaborator = collaborator)
    interested_project_ids = interests.values_list("project_id", flat = True)
    
    return render(request, "core/collaborator.html", {"ranked_projects": ranked_projects, "interested_project_ids": interested_project_ids, "collaborator": collaborator, "collaborator_skills": collaborator_skills, "sector_interests_display": sector_interests_display})

def collaborator_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        form = forms.CollaboratorForm(request.POST)
        skill_formset = forms.CollaboratorSkillFormSet(request.POST)

        if form.is_valid() and skill_formset.is_valid():
            availability = form.cleaned_data["availability"]
            commitment = form.cleaned_data["commitment"]
            sector_interests = form.cleaned_data["sector_interests"]

            user = request.user

            #Spara information från användare i respektive databas
            profile = Profile.objects.get(user = user)
            collaborator, created = Collaborator_profile.objects.update_or_create(profile = profile, defaults = {"availability": availability, "commitment": commitment, "sector_interests": sector_interests})

            for skill_form in skill_formset:
                if skill_form.cleaned_data:
                    skill = skill_form.cleaned_data["skill"]
                    proficiency = skill_form.cleaned_data["proficiency"]

                    Collaborator_skill.objects.update_or_create(collaborator = collaborator, skill = skill, defaults = {"proficiency": proficiency})

            return redirect("collaborator")
    else:
        profile = Profile.objects.get(user = request.user)

        try:
            collaborator = Collaborator_profile.objects.get(profile = profile)

            form = forms.CollaboratorForm(initial = {"availability": collaborator.availability, "commitment": collaborator.commitment, "sector_interests": collaborator.sector_interests})

            collaborator_skills = Collaborator_skill.objects.filter(collaborator = collaborator)

            skills_initial = []

            for collaborator_skill in collaborator_skills:
                skills_initial.append({"skill": collaborator_skill.skill, "proficiency": collaborator_skill.proficiency})

            skill_formset = forms.CollaboratorSkillFormSet(initial = skills_initial)

        except Collaborator_profile.DoesNotExist:
            form = forms.CollaboratorForm()
            skill_formset = forms.CollaboratorSkillFormSet()

    return render(request, "core/collaborator_profile.html", {"collaborator_form": form, "skill_formset": skill_formset})

def idea_maker_profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    user = request.user
    profile = Profile.objects.get(user = user)
    idea_maker, created = Idea_maker_profile.objects.get_or_create(profile = profile)
    projects = Project.objects.filter(idea_maker = idea_maker)

    if request.method == "POST":
        form = forms.IdeaMakerForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data["bio"]

            idea_maker.bio = bio
            idea_maker.save()

            return redirect("idea_maker_profile")
    else:
        form = forms.IdeaMakerForm(initial = {"bio": idea_maker.bio})

    return render(request, "core/idea_maker_profile.html", {"idea_maker_form": form, "idea_maker": idea_maker, "projects": projects})

def create_project(request):
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    profile = Profile.objects.get(user = user)
    idea_maker = Idea_maker_profile.objects.get(profile = profile)

    if request.method == "POST":
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            req_hours = form.cleaned_data["req_hours"]
            description = form.cleaned_data["description"]
            category = form.cleaned_data["category"]
            compensation = form.cleaned_data["compensation"]
            stage = form.cleaned_data["stage"]

            project = Project.objects.create(name = name, req_hours = req_hours, description = description, category = category, compensation = compensation, stage = stage, idea_maker = idea_maker)

            return redirect("project_requirements", project_id = project.id)
    else:
        form = forms.ProjectForm()

    return render(request, "core/create_project.html", {"project_form": form})

def project_requirements(request, project_id):
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    profile = Profile.objects.get(user = user)
    idea_maker = Idea_maker_profile.objects.get(profile = profile)

    project = Project.objects.get(id = project_id, idea_maker = idea_maker)

    if request.method == "POST":
        role_form = forms.ProjectRoleForm(request.POST)
        skill_formset = forms.ProjectSkillFormSet(request.POST)

        if role_form.is_valid() and skill_formset.is_valid():
            role = role_form.cleaned_data["role"]

            project_role, created = Project_role.objects.get_or_create(project = project, role = role)

            for skill_form in skill_formset:
                if skill_form.cleaned_data:
                    skill = skill_form.cleaned_data["skill"]
                    required_proficiency = skill_form.cleaned_data["required_proficiency"]

                    Project_skill.objects.update_or_create(project_role = project_role, skill = skill, defaults = {"required_proficiency": required_proficiency})

            return redirect("project_requirements", project_id = project.id)
    else:
        role_form = forms.ProjectRoleForm()
        skill_formset = forms.ProjectSkillFormSet()

    return render(request, "core/project_requirements.html", {"project": project, "role_form": role_form, "skill_formset": skill_formset})
    
def delete_project(request, project_id):
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    profile = Profile.objects.get(user = user)
    idea_maker = Idea_maker_profile.objects.get(profile = profile)

    project = Project.objects.get(idea_maker = idea_maker, id = project_id)

    project.delete()

    return redirect('idea_maker_profile')

def show_interest(request, project_id):
    if not request.user.is_authenticated:
        return redirect("login")

    user = request.user
    profile = Profile.objects.get(user = user)
    collaborator = Collaborator_profile.objects.get(profile = profile)

    project = Project.objects.get(id = project_id)

    Project_interest.objects.get_or_create(collaborator = collaborator, project = project)

    return redirect("collaborator")