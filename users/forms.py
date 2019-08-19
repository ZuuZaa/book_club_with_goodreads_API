from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50, label = "Adınız " )
    last_name = forms.CharField(max_length = 50, label = "Soyadınız ")
    username = forms.EmailField(max_length = 50, label = "E-mail adresiniz ")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 50, label = "Adınız " )
    last_name = forms.CharField(max_length = 50, label = "Soyadınız ")
    username = forms.EmailField(max_length = 50, label = "E-mail adresiniz ")

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
        ]

class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        widgets = {'bday' : DateInput()}
        fields = [
            'image',
            'bio',
            'bday',
            'genre'
        ]
