from django.contrib import admin
from .models import Insumo, Receta, Ingrediente, MenuDiario, CalculoInsumos

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'unidad')
    search_fields = ('codigo', 'nombre')

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'temporada', 'tipo_comida', 'porciones')
    search_fields = ('codigo', 'nombre')
    list_filter = ('temporada', 'tipo_comida')

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('receta', 'insumo', 'cantidad')
    search_fields = ('receta__nombre', 'insumo__nombre')
    list_filter = ('receta', 'insumo')

@admin.register(MenuDiario)
class MenuDiarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipo_comida', 'receta', 'temporada', 'comensales')
    search_fields = ('receta__nombre',)
    list_filter = ('fecha', 'tipo_comida', 'temporada')
    fields = ('fecha', 'tipo_comida', 'receta', 'temporada', 'comensales')

@admin.register(CalculoInsumos)
class CalculoInsumosAdmin(admin.ModelAdmin):
    list_display = ('fecha_calculo', 'fecha_inicio', 'fecha_fin', 'temporada')
    search_fields = ('fecha_inicio', 'fecha_fin')
    list_filter = ('fecha_calculo', 'temporada')