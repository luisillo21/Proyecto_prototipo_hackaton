from .models import *
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres',
                  'apellidos',
                  'correo',
                  'clave',
                  ]

        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo': 'Email',
            'clave': 'Contraseña',
        }
        widgets = {
            'nombres': forms.TextInput(attrs={"class": "form-control text-dark", "type": "text", "placeholder": "Ingrese su nombre"}),
            'apellidos': forms.TextInput(attrs={"class": "form-control text-dark", "type": "text", "placeholder": "Ingrese su apellido"}),
            'correo': forms.TextInput(attrs={"class": "form-control text-dark", "type": "email", "placeholder": "Ingrese su correo"}),
            "clave": forms.TextInput(attrs={"class": "form-control", "type": "password", "placeholder": "Ingrese su contraseña"})
        }



