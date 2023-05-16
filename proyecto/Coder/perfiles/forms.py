from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    #Esto es un model form
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)

class Meta:
    model=User
    fields=['last_name','first_name','username','email','password1','password2']

