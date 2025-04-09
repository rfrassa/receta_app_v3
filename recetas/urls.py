from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    InsumoViewSet, RecetaViewSet, IngredienteViewSet, MenuDiarioViewSet,
    calcular_insumos_web, exportar_insumos_excel, agregar_insumo, agregar_receta,
    agregar_ingrediente, agregar_menu_diario, historico_calculos
)

# Configuración del router para las rutas de la API (DRF)
router = DefaultRouter()
router.register(r'insumos', InsumoViewSet)
router.register(r'recetas', RecetaViewSet)
router.register(r'ingredientes', IngredienteViewSet)
router.register(r'menu-diario', MenuDiarioViewSet)

# Namespace para las URLs
app_name = 'recetas'

# Definición de las URLs
urlpatterns = [
    # Ruta para la página principal
    path('', views.index, name='index'),  # Nueva ruta para la página principal

    # Rutas de la API (DRF)
    path('api/', include(router.urls)),  # Prefijo 'api/' para las rutas de DRF

    # Rutas para vistas renderizadas
    path('calcular-insumos/', calcular_insumos_web, name='calcular_insumos'),  # Unificamos y corregimos el nombre
    path('exportar-excel/', exportar_insumos_excel, name='exportar_insumos_excel'),
    path('agregar-insumo/', agregar_insumo, name='agregar_insumo'),
    path('agregar-receta/', agregar_receta, name='agregar_receta'),
    path('agregar-ingrediente/', agregar_ingrediente, name='agregar_ingrediente'),
    path('agregar-menu-diario/', agregar_menu_diario, name='agregar_menu_diario'),
    path('historico-calculos/', historico_calculos, name='historico_calculos'),
    path('receta/<int:receta_id>/', views.ver_receta_completa, name='ver_receta_completa'),

    # Rutas para las plantillas que faltaban
    path('listar-urls/', views.listar_urls, name='listar_urls'),  # Nueva ruta para listar_urls.html
    path('cargar-insumo/', views.cargar_insumo, name='cargar_insumo'),  # Nueva ruta para cargar_insumo.html
    path('cargar-receta/', views.cargar_receta, name='cargar_receta'),  # Nueva ruta para cargar_receta.html
]