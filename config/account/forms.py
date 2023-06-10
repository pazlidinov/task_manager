from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class ProfileUserCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','birthday','direction', 'phone_number', 'password', 'username']
        widgets = {
            'first_name':forms.TextInput(attrs={"class":"main__form--input"}),
            'last_name':forms.TextInput(attrs={"class":"main__form--input"}),
            'birthday':forms.DateInput(attrs={"class":"main__form--input", "type":"date", 'placeholder':'sana'}),
            'direction':forms.SelectMultiple(attrs={"class":"main__form--input"}),
            'phone_number':forms.TextInput(attrs={"class":"main__form--input"}),           
            'password':forms.PasswordInput(attrs={"class":"main__form--input"}),
            'password2':forms.PasswordInput(attrs={"class":"main__form--input"}),
        }

