# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from forms import SignUpForm, LoginForm
from models import UserModel, SessionToken
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout, get_user_model



# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #Hashing the password
            password = make_password(password)

            #saving data to DB
            user = UserModel(name=name, password=make_password(password), email=email, username=username)
            user.save()
            return redirect('login/')
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form' : form})


def login_view(request):
    dict = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print username, password
            user = UserModel.objects.filter(username=username).first()

            if user:
                # Check for the password
                if not check_password(password, user.password):
                    dict['message'] = 'Incorrect Password! Please try again!'
                else:
                    token = SessionToken(user=user)
                    token.create_token()
                    token.save()
                    return redirect('feed/', token.objects.filter(user=user).first())
    else:
        form = LoginForm()

    dict['form'] = form
    return render(request, 'login.html', dict)

def feed_view(request):
    return render(request, 'feed.html', {})

