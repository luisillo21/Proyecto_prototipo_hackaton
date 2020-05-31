from .models import *
from django import forms


class Cosecha_1(forms.ModelForm):
    class Meta:
        model = Cosecha
        fields = ['tipo_cosecha',
                  'nombre_cosecha',
                  'descripcion',
                  'vitamina',
                  'temperatura',
                  'tiempo_de_riego',
                  'humedad_de_tierra',
                  ]

        labels={
            'tipo_cosecha':'Tipo',
            'nombre_cosecha':'Codigo',
            'descripcion':'Descripcion',
            'vitamina':'Vitamina',
            'temperatura':'Temperatura',
            'tiempo_de_riego':'Tiempo de riego',
            'humedad_de_tierra':'humedad de tierra',
        }

        widgets = {

            'tipo_cosecha': forms.TextInput(attrs={'class':'from-control',"placeholder": "Ingrese el tipo"}),
            'nombre_cosecha': forms.TextInput(attrs={'class':'from-control',"placeholder": "Ingrese el nombre de la cosecha"}),
            'descripcion': forms.TextInput(attrs={'class':'from-control',"placeholder": "Ingrese una descripcion"}),
            'vitamina': forms.TextInput(attrs={'class': 'from-control', "placeholder": "Ingrese vitamina"}),
            'temperatura': forms.TextInput(attrs={'class': 'from-control', "placeholder": "Ingrese temperatura"}),
            'tiempo_de_riego': forms.TextInput(attrs={'class': 'from-control', "placeholder": "Ingrese tiempo de riego"}),
            'humedad_de_tierra': forms.TextInput(attrs={'class': 'from-control', "placeholder": "Ingrese la humedad de la tierra"}),
        }
