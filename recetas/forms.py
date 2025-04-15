# recetas/forms.py

from django import forms
from .models import Insumo, Receta, Ingrediente, MenuDiario #MenuDiarioMultiple


# 👉 Formulario para Agregar y Editar Insumos
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'unidad', 'presentacion']
        widgets = {
            'presentacion': forms.TextInput(attrs={'placeholder': 'Ej: 400 gramos, 1 litro, 1 unidad'}),
        }

# 👉 Formulario para Agregar y Editar Recetas
class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['codigo', 'nombre', 'temporada', 'tipo_comida', 'imagen']

# 👉 Formulario para Agregar y Editar Ingredientes
class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['insumo', 'receta', 'cantidad']

# 👉 Formulario para Agregar Menú Diario "uno por uno"
class MenuDiarioForm(forms.ModelForm):
    class Meta:
        model = MenuDiario
        fields = ['fecha', 'receta', 'temporada', 'comensales']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'unidad', 'presentacion']
        widgets = {
            'presentacion': forms.TextInput(attrs={'placeholder': 'Ej: 400 gramos, 1 litro, 1 unidad'}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['codigo', 'nombre', 'temporada', 'tipo_comida', 'imagen']

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['insumo', 'receta', 'cantidad']

class MenuDiarioForm(forms.ModelForm):
    class Meta:
        model = MenuDiario
        fields = ['fecha', 'receta', 'temporada', 'comensales']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }


class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['codigo', 'nombre', 'unidad', 'presentacion']
        widgets = {
            'presentacion': forms.TextInput(attrs={'placeholder': 'Ej: 400 gramos, 1 litro, 1 unidad'}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['codigo', 'nombre', 'temporada', 'tipo_comida', 'imagen']

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['insumo', 'receta', 'cantidad']

class MenuDiarioForm(forms.ModelForm):
    class Meta:
        model = MenuDiario
        fields = ['fecha', 'receta', 'temporada', 'comensales']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class MenuDiarioMultipleForm(forms.Form):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha'
    )

    desayuno = forms.ModelChoiceField(
        queryset=Receta.objects.filter(tipo_comida='desayuno'),
        required=False,
        label='Receta Desayuno'
    )
    comensales_desayuno = forms.IntegerField(required=False, initial=0, label='Comensales Desayuno')

    merienda = forms.ModelChoiceField(
        queryset=Receta.objects.filter(tipo_comida='merienda'),
        required=False,
        label='Receta Merienda'
    )
    comensales_merienda = forms.IntegerField(required=False, initial=0, label='Comensales Merienda')

    almuerzo = forms.ModelChoiceField(
        queryset=Receta.objects.filter(tipo_comida='almuerzo'),
        required=False,
        label='Receta Almuerzo'
    )
    comensales_almuerzo = forms.IntegerField(required=False, initial=0, label='Comensales Almuerzo')

    cena = forms.ModelChoiceField(
        queryset=Receta.objects.filter(tipo_comida='cena'),
        required=False,
        label='Receta Cena'
    )
    comensales_cena = forms.IntegerField(required=False, initial=0, label='Comensales Cena')
