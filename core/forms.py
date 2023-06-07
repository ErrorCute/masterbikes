from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import Usuario
import datetime
from django.contrib.auth.forms import UserCreationForm



class UsuarioUserForm(UserCreationForm):
    pass


