from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InsumoViewSet, RecetaViewSet, IngredienteViewSet, MenuDiarioViewSet,
    calcular_insumos_web, exportar_insumos_excel, agregar_insumo, agregar_receta,
    agregar_ingrediente, agregar_menu_diario, historico_calculos
)

router = DefaultRouter()
router.register(r'insumos', InsumoViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'menu-diario', MenuDiarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calcular/', calcular_insumos_web, name='calcular_insumos_web'),
    path('exportar-excel/', exportar_insumos_excel, name='exportar_insumos_excel'),
    path('agregar-insumo/', agregar_insumo, name='agregar_insumo'),
    path('agregar-receta/', agregar_receta, name='agregar_receta'),
    path('agregar-ingrediente/', agregar_ingrediente, name='agregar_ingrediente'),
    path('agregar-menu-diario/', agregar_menu_diario, name='agregar_menu_diario'),
    path('historico-calculos/', historico_calculos, name='historico_calculos'),
]