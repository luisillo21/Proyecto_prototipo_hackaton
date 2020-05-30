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
            'nombres': forms.TextInput(attrs={"class": "form-control text-dark", "type": "text"}),
            'apellidos': forms.TextInput(attrs={"class": "form-control text-dark", "type": "text"}),
            'correo': forms.TextInput(attrs={"class": "form-control text-dark", "type": "email"}),
            "clave": forms.TextInput(attrs={"class": "form-control", "type": "password"})
        }



