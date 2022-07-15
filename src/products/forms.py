from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','image','describe','if_infected')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','image','describe','if_infected')