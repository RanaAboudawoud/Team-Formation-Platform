from django import forms
from django.contrib.auth.models import User
from .models import Profile, Skill, Collaborator_skill, Project_skill, Project, Project_role, Collaborator_profile

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    phone_number = forms.CharField(max_length=20)
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)
    role = forms.ChoiceField(
        choices = Profile.ROLE_CHOICES,
        widget = forms.RadioSelect
        )

    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("This username is already taken.")

        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 200)
    password = forms.CharField(widget = forms.PasswordInput)

class CollaboratorForm(forms.Form):
    availability = forms.ChoiceField(choices = Collaborator_profile.AVAILABILITY_CHOICES)
    commitment = forms.ChoiceField(choices = Collaborator_profile.COMMITMENT_CHOICES)
    sector_interests = forms.MultipleChoiceField(choices = Project.SECTOR_CHOICES, widget = forms.CheckboxSelectMultiple)

class CollaboratorSkillForm(forms.Form):
    skill = forms.ModelChoiceField(queryset = Skill.objects.all())
    proficiency = forms.ChoiceField(choices = Project_skill.PROFICIENCY_CHOICES)

CollaboratorSkillFormSet = forms.formset_factory(CollaboratorSkillForm, extra = 1)

class IdeaMakerForm(forms.Form):
    bio = forms.CharField(widget = forms.Textarea, max_length = 1000)

class ProjectForm(forms.Form):
    name = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000, widget = forms.Textarea)
    req_hours = forms.ChoiceField(choices = Project.REQ_HOURS_CHOICES, label = "Expected Availability:")
    sector = forms.ChoiceField(choices = Project.SECTOR_CHOICES)
    compensation = forms.ChoiceField(choices = Project.COMPENSATION_CHOICES)
    stage = forms.ChoiceField(choices = Project.STAGE_CHOICES)
    commitment = forms.ChoiceField(choices = Collaborator_profile.COMMITMENT_CHOICES)

class ProjectRoleForm(forms.Form):
    role = forms.ChoiceField(choices = Project_role.ROLE_CHOICES)

class ProjectSkillForm(forms.Form):
    skill = forms.ModelChoiceField(queryset = Skill.objects.all())
    required_proficiency = forms.ChoiceField(choices = Project_skill.PROFICIENCY_CHOICES)

ProjectSkillFormSet = forms.formset_factory(ProjectSkillForm, extra = 0, min_num = 1, validate_min = True)