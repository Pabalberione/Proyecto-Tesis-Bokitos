from pyexpat import model
from tkinter import Widget
from typing_extensions import Required
from django import forms
from django.forms import ModelForm
from .models import proveedor

class añadirProveedor(ModelForm):
    nombre = forms.TextInput()
    direccion = forms.TextInput()
    ciudad = forms.TextInput()
    telefono = forms.TextInput()
    codigo_postal = forms.TextInput()
    email = forms.EmailField()

    class Meta:
        model = proveedor
        fields = ['nombre', 'direccion', 'ciudad', 'telefono', 'codigo_postal', 'email']

    #VER EL VIDEO DE LOS WIDGETS DEL PELADO PARA AGREGARLE UN FORMATO AL FORM 