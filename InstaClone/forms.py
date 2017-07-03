from django import forms
from django.forms import ModelForm
from models import UserModel, LoginModel
from django.contrib.auth import authenticate, login, logout, get_user_model

class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields=['email','username','name','password']

class LoginForm(ModelForm):
    class Meta:
        model = LoginModel
        fields = ['username', 'password']
