from django import forms
from django.contrib.auth.models import User
from .models import Profile, Skill, Collaborator_skill, Project_skill

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

class CollaboratorForm(forms.Form):
    skill = forms.ModelChoiceField(queryset = Skill.objects.all())
    proficiency = forms.ChoiceField(choices = Project_skill.PROFICIENCY_CHOICES)
    availability = forms.IntegerField(min_value = 0)