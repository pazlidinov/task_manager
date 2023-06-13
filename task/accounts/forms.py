from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import Profile


class LoginForm(forms.ModelForm):
    # Login form for django standart user model

    class Meta:

        model = Profile
        fields = ["username", "password"]


class RegistrationForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ['username', 'birthday', 'direction',
                  'phone_number', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={"class": "main__form--input", 'placeholder': 'Login'}),
            'birthday': forms.DateInput(attrs={"class": "main__form--input", "type": "text", 'placeholder': "Tug'ilgan sana", "onfocus": "(this.type='date')", 'onblur': "(this.type='text')"}),
            'direction': forms.SelectMultiple(attrs={"class": "main__form--input", 'size': '1', 'placeholder': "Yo'nalish"}),
            'phone_number': forms.TextInput(attrs={"class": "main__form--input", 'placeholder': 'Telefon *'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name','last_name','birthday', 'img', 'facebook_link', 'instagram_link', 'telegram_link']
        # widgets = {
        #     'birthday':forms.DateInput()
        # }
