from django import forms
from django.forms import ModelForm
from django.forms import fields

import datetime
from.models import SolicitudArriendo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UsuarioUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]




class Nuevasolicitud(ModelForm):

     class Meta:
        model = SolicitudArriendo
        fields = ["id_arriendo","bicicleta","fecha_arriendo","cantidad"]


class Modificarestado(ModelForm):
     class Meta:
        model = SolicitudArriendo
        fields = ["estado"]        