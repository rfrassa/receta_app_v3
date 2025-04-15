from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    

    # Recetas
    path('agregar-receta/', views.agregar_receta, name='agregar_receta'),
    path('gestionar-recetas/', views.gestionar_recetas, name='gestionar_recetas'),
    path('importar-recetas/', views.importar_recetas, name='importar_recetas'),
    path('agregar-receta/', views.agregar_receta, name='receta_list'),

    # Gestión de recetas individuales
    path('recetas/<int:receta_id>/', views.ver_receta_completa, name='ver_receta_completa'),
    path('recetas/<int:receta_id>/editar/', views.receta_edit, name='receta_edit'),
    path('recetas/<int:receta_id>/eliminar/', views.receta_delete, name='receta_delete'),
    path('recetas/<int:receta_id>/exportar-pdf/', views.exportar_receta_pdf, name='exportar_receta_pdf'),
    path('recetas/<int:receta_id>/favorito/', views.toggle_favorito, name='toggle_favorito'),

    # Confirmación de borrado (usa mismo path que receta_delete porque ahora chequea POST)
    # No cambia la ruta.

    # Ingredientes
    path('recetas/<int:receta_id>/agregar-ingrediente/', views.agregar_ingrediente, name='agregar_ingrediente'),
    path('importar-ingredientes/', views.importar_ingredientes, name='importar_ingredientes'),
    path('ingredientes/', views.ingredientes_list, name='ingredientes_list'),
    path('ingredientes/<int:ingrediente_id>/editar/', views.editar_ingrediente, name='editar_ingrediente'),
    path('ingredientes/<int:ingrediente_id>/eliminar/', views.eliminar_ingrediente, name='eliminar_ingrediente'),

    # Menú Diario
    path('agregar-menu-diario/', views.agregar_menu_diario, name='agregar_menu_diario'),
    #path('cargar-menu-multiple/', views.cargar_menu_multiple, name='cargar_menu_multiple'),
    path('agregar-menu-multiple/', views.agregar_menu_multiple, name='agregar_menu_multiple'),
    path('menu-diario/<int:menu_id>/borrar/', views.borrar_menu_diario, name='borrar_menu_diario'),

    
    


    # Cálculo de insumos
    path('calcular-insumos/', views.calcular_insumos_web, name='calcular_insumos_web'),
    path('exportar-excel/', views.exportar_insumos_excel, name='exportar_insumos_excel'),
    path('historico-calculos/', views.historico_calculos, name='historico_calculos'),
    path('borrar-calculo/<int:calculo_id>/', views.borrar_calculo, name='borrar_calculo'),
    


# Insumos
    # path('agregar-insumo/', views.agregar_insumo, name='agregar_insumo'),
    path('importar-insumos/', views.importar_insumos, name='importar_insumos'),
    path('agregar-insumo/', views.agregar_insumo, name='agregar_insumo'),
    
    
    # Comentarios
    path('recetas/<int:receta_id>/comentar/', views.agregar_comentario, name='agregar_comentario'),
    path('comentarios/<int:comentario_id>/responder/', views.responder_comentario, name='responder_comentario'),
    path('comentarios/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),

    # Favoritos y Notificaciones
    path('recetas/favoritos/', views.favoritos_list, name='favoritos_list'),
    path('recetas/notificaciones/', views.notificaciones_list, name='notificaciones_list'),

    # Utilidades
    path('listar-urls/', views.listar_urls, name='listar_urls'),
    path('backup/', views.backup_bd, name='backup_bd'),
    path('historico-calculos/<int:calculo_id>/borrar/', views.borrar_calculo, name='borrar_calculo'),
    path('historico-calculos/<int:calculo_id>/ver/', views.ver_calculo, name='ver_calculo'),
    path('historico-calculos/<int:calculo_id>/', views.ver_calculo, name='ver_calculo'),


]
