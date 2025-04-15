# recetas/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import json

class Insumo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20, default='kg')
    presentacion = models.DecimalField(max_digits=10, decimal_places=2, default=1)  # 👈 NUEVO CAMPO
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='insumos')

    def __str__(self):
        return f"{self.nombre} ({self.unidad})"

class Receta(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    tipo_comida = models.CharField(max_length=20, choices=(('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('merienda', 'Merienda'), ('cena', 'Cena')))
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='recetas')
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.temporada} - {self.tipo_comida})"

class Ingrediente(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name='ingredientes')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name="ingredientes")
    cantidad = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='ingredientes')

    def __str__(self):
        return f"{self.insumo.nombre} - {self.cantidad} {self.insumo.unidad} para {self.receta.nombre}"

class MenuDiario(models.Model):
    fecha = models.DateField()
    tipo_comida = models.CharField(max_length=20, choices=(('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('merienda', 'Merienda'), ('cena', 'Cena')))
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='menus')
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    comensales = models.PositiveIntegerField(default=115)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='menus')

    def __str__(self):
        return f"{self.fecha} - {self.tipo_comida} - {self.receta.nombre} ({self.temporada}) - {self.comensales} comensales"

    def clean(self):
        if self.receta.tipo_comida != self.tipo_comida:
            raise ValidationError(
                f"El tipo de comida de la receta ({self.receta.tipo_comida}) no coincide con el tipo de comida del menú ({self.tipo_comida})."
            )

    class Meta:
        unique_together = ('fecha', 'tipo_comida', 'temporada')

class CalculoInsumos(models.Model):
    fecha_calculo = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    insumos = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='calculos')

    def __str__(self):
        return f"Cálculo del {self.fecha_calculo} para {self.fecha_inicio} a {self.fecha_fin} ({self.temporada})"

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='favoritos')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.receta.nombre}"

    class Meta:
        unique_together = ('usuario', 'receta')

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respuestas')

    def __str__(self):
        return f"Comentario de {self.usuario.username} en {self.receta.nombre}"

class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

    def __str__(self):
        return f"Notificación para {self.usuario.username}: {self.mensaje}"