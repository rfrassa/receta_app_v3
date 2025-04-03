from django import forms
from .models import Insumo, Receta, Ingrediente, MenuDiario

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'unidad']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['codigo', 'nombre', 'temporada', 'tipo_comida', 'porciones']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'temporada': forms.Select(attrs={'class': 'form-control'}),
            'tipo_comida': forms.Select(attrs={'class': 'form-control'}),
            'porciones': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['receta', 'insumo', 'cantidad']
        widgets = {
            'receta': forms.Select(attrs={'class': 'form-control'}),
            'insumo': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class MenuDiarioForm(forms.ModelForm):
    class Meta:
        model = MenuDiario
        fields = ['fecha', 'tipo_comida', 'receta', 'temporada', 'comensales']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tipo_comida': forms.Select(attrs={'class': 'form-control'}),
            'receta': forms.Select(attrs={'class': 'form-control'}),
            'temporada': forms.Select(attrs={'class': 'form-control'}),
            'comensales': forms.NumberInput(attrs={'class': 'form-control'}),
        }