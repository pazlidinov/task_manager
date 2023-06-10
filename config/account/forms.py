from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','birthday','direction', 'phone_number', "password1", "password2"]
        
