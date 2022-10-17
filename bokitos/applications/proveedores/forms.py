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
    email = forms.TextInput()

    class Meta:
        model = proveedor
        fields = ['nombre', 'direccion', 'ciudad', 'telefono', 'codigo_postal', 'email']

    #VER EL VIDEO DE LOS WIDGETS DEL PELADO PARA AGREGARLE UN FORMATO AL FORM 
        labels = {
            'nombre': '',
            'direccion':'',
            'ciudad':'',
            'telefono':'',
            'codigo_postal':'',
            'email':'',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'direccion':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}),
            'telefono':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Teléfono'}),
            'codigo_postal':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Código postal'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),

        }