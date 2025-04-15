# recetas/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'recetas', views.RecetaViewSet)
router.register(r'insumos', views.InsumoViewSet)
router.register(r'ingredientes', views.IngredienteViewSet)
router.register(r'menus', views.MenuDiarioViewSet)

app_name = 'recetas_api'

urlpatterns = [
    path('', include(router.urls)),
]