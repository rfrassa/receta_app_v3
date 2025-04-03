from rest_framework import serializers
from .models import Insumo, Receta, Ingrediente, MenuDiario

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ['id', 'codigo', 'nombre', 'unidad']

class IngredienteSerializer(serializers.ModelSerializer):
    insumo = InsumoSerializer(read_only=True)
    insumo_id = serializers.PrimaryKeyRelatedField(queryset=Insumo.objects.all(), source='insumo', write_only=True)

    class Meta:
        model = Ingrediente
        fields = ['id', 'insumo', 'insumo_id', 'cantidad']

class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Receta
        fields = ['id', 'codigo', 'nombre', 'temporada', 'tipo_comida', 'porciones', 'ingredientes']

class MenuDiarioSerializer(serializers.ModelSerializer):
    receta = RecetaSerializer(read_only=True)
    receta_id = serializers.PrimaryKeyRelatedField(queryset=Receta.objects.all(), source='receta', write_only=True)

    class Meta:
        model = MenuDiario
        fields = ['id', 'fecha', 'tipo_comida', 'receta', 'receta_id', 'temporada', 'comensales']