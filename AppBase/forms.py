from django import forms
from .models import *

TIPO_OPCIONES = [('nafta', 'Nafta'), ('diesel', 'Diesel'), ('electrico', 'Electrico'), ('hibrido', 'Hibrido'),]
TIPO_OPCIONES = sorted(TIPO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class AutosForm(forms.Form):
    modelo = forms.CharField(max_length=255)
    fecha_salida = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    tipo = forms.CharField(max_length=255, widget=forms.Select(choices=TIPO_OPCIONES))
    marca = forms.CharField(max_length=255)
    descripcion = forms.CharField(max_length=255)
    valoracion = forms.IntegerField(required=True, widget=forms.Select(choices=VALORACIONES_OPCIONES))

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ('__all__')

class BuscarModelo(forms.Form):
    modelo = forms.CharField(label='Modelo del auto', max_length=255)

class BuscarTipo(forms.Form):
    tipo = forms.CharField(label='Nombre del tipo', max_length=255, widget=forms.Select(choices=TIPO_OPCIONES))

class BuscarMarca(forms.Form):
    marca = forms.CharField(label='Nombre de la marca', max_length=255)

class BuscarValoracion(forms.Form):
    valoracion = forms.IntegerField(label='Valoracion', widget=forms.Select(choices=VALORACIONES_OPCIONES))

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']