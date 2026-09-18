from django import forms
from .models import Profile

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