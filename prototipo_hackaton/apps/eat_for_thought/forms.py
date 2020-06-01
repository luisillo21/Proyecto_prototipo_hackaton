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
            'humedad_de_tierra':'Humedad de tierra',
        }

        widgets = {

            'tipo_cosecha': forms.TextInput(attrs={'class':'from-control',"placeholder": "Fruta o Vegetales"}),
            'nombre_cosecha': forms.TextInput(attrs={'class':'from-control',"placeholder": ""}),
            'descripcion': forms.TextInput(attrs={'class':'from-control',"placeholder": ""}),
            'vitamina': forms.TextInput(attrs={'class': 'from-control', "placeholder": ""}),
            'temperatura': forms.TextInput(attrs={'class': 'from-control', "placeholder": ""}),
            'tiempo_de_riego': forms.TextInput(attrs={'class': 'from-control', "placeholder": ""}),
            'humedad_de_tierra': forms.TextInput(attrs={'class': 'from-control', "placeholder": ""}),
        }
