from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from datetime import datetime
from openpyxl import Workbook
import json
from .models import Insumo, Receta, Ingrediente, MenuDiario, CalculoInsumos
from .serializers import InsumoSerializer, RecetaSerializer, IngredienteSerializer, MenuDiarioSerializer
from .forms import InsumoForm, RecetaForm, IngredienteForm, MenuDiarioForm
from .models import Receta
from django.shortcuts import render, redirect, get_object_or_404  # Consolidado aquí
from django.urls import get_resolver



class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class MenuDiarioViewSet(viewsets.ModelViewSet):
    queryset = MenuDiario.objects.all()
    serializer_class = MenuDiarioSerializer

    @action(detail=False, methods=['get'])
    def calcular_insumos(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        temporada = request.query_params.get('temporada', 'verano')

        try:
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
        except (ValueError, TypeError):
            return Response({"error": "Formato de fecha inválido. Use YYYY-MM-DD."}, status=400)

        menus = MenuDiario.objects.filter(fecha__range=[fecha_inicio, fecha_fin], temporada=temporada)
        insumos_necesarios = {}

        for menu in menus:
            receta = menu.receta
            factor = menu.comensales / receta.porciones
            ingredientes = Ingrediente.objects.filter(receta=receta)
            for ingrediente in ingredientes:
                insumo = ingrediente.insumo
                cantidad = ingrediente.cantidad * factor
                if insumo.nombre in insumos_necesarios:
                    insumos_necesarios[insumo.nombre] += cantidad
                else:
                    insumos_necesarios[insumo.nombre] = cantidad

        resultado = [
            {
                'codigo': Insumo.objects.get(nombre=nombre).codigo,
                'insumo': nombre,
                'cantidad': round(cantidad, 2),
                'unidad': Insumo.objects.get(nombre=nombre).unidad
            }
            for nombre, cantidad in insumos_necesarios.items()
        ]

        # Guardar el cálculo en el historial
        CalculoInsumos.objects.create(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            temporada=temporada,
            insumos=json.dumps(resultado)
        )

        return Response(resultado)

def agregar_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_insumo')
    else:
        form = InsumoForm()
    return render(request, 'recetas/agregar_insumo.html', {'form': form})

def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_receta')
    else:
        form = RecetaForm()
    return render(request, 'recetas/agregar_receta.html', {'form': form})

def agregar_ingrediente(request):
    if request.method == 'POST':
        form = IngredienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_ingrediente')
    else:
        form = IngredienteForm()
    return render(request, 'recetas/agregar_ingrediente.html', {'form': form})

def agregar_menu_diario(request):
    if request.method == 'POST':
        form = MenuDiarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_menu_diario')
    else:
        form = MenuDiarioForm()
    return render(request, 'recetas/agregar_menu_diario.html', {'form': form})

def calcular_insumos_web(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    temporada = request.GET.get('temporada', 'verano')

    insumos = []
    menus = []
    if fecha_inicio and fecha_fin:
        url = 'http://127.0.0.1:8000/api/menu-diario/calcular_insumos/'
        params = {'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'temporada': temporada}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            insumos = response.json()
        
        # Obtener los menús diarios para mostrar las recetas
        from .models import MenuDiario
        menus = MenuDiario.objects.filter(fecha__range=[fecha_inicio, fecha_fin], temporada=temporada)

    return render(request, 'recetas/calcular_insumos.html', {
        'insumos': insumos,
        'menus': menus,  # Añadido
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'temporada': temporada
    })
    
def exportar_insumos_excel(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    temporada = request.GET.get('temporada', 'verano')

    url = 'http://127.0.0.1:8000/api/menu-diario/calcular_insumos/'
    params = {'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin, 'temporada': temporada}
    response = requests.get(url, params=params)
    insumos = response.json() if response.status_code == 200 else []

    wb = Workbook()
    ws = wb.active
    ws.title = "Insumos Necesarios"
    ws.append(['Código', 'Insumo', 'Cantidad', 'Unidad'])
    for item in insumos:
        ws.append([item['codigo'], item['insumo'], item['cantidad'], item['unidad']])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="insumos_{fecha_inicio}_a_{fecha_fin}.xlsx"'
    wb.save(response)
    return response

def historico_calculos(request):
    calculos = CalculoInsumos.objects.all().order_by('-fecha_calculo')
    return render(request, 'recetas/historico_calculos.html', {'calculos': calculos})


from django.urls import get_resolver

def ver_receta_completa(request, receta_id):
    # Obtener la receta o devolver 404 si no existe
    receta = get_object_or_404(Receta, id=receta_id)
  # Obtener todos los ingredientes asociados a la receta
    ingredientes = receta.ingredientes.all()
    # Contexto para la plantilla
    context = {
        'receta': receta,
        'ingredientes': ingredientes,
    }
    
    return render(request, 'recetas/ver_receta_completa.html', context)

def listar_urls(request):
    urls = []

    def extract_urls(url_patterns, prefix=''):
        for pattern in url_patterns:
            if hasattr(pattern, 'url_patterns'):
                # Es un include(), seguimos explorando
                extract_urls(pattern.url_patterns, prefix + str(pattern.pattern))
            else:
                # Es una URL final
                full_url = prefix + str(pattern.pattern)
                urls.append({
                    'url': full_url,
                    'name': pattern.name if pattern.name else 'Sin nombre',
                    'view': str(pattern.callback) if pattern.callback else 'Sin vista'
                })

    # Obtener todas las URLs del proyecto
    extract_urls(get_resolver().url_patterns)

    return render(request, 'recetas/listar_urls.html', {'urls': urls})

