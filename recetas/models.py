from django.db import models
from django.core.exceptions import ValidationError
import json

class Insumo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20, default='kg')

    def __str__(self):
        return f"{self.nombre} ({self.unidad})"

class Receta(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    tipo_comida = models.CharField(max_length=20, choices=(('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('merienda', 'Merienda'), ('cena', 'Cena')))
    porciones = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} ({self.temporada} - {self.tipo_comida})"

class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='ingredientes')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.FloatField()

    def __str__(self):
        return f"{self.insumo.nombre} - {self.cantidad} {self.insumo.unidad} para {self.receta.nombre}"

class MenuDiario(models.Model):
    fecha = models.DateField()
    tipo_comida = models.CharField(max_length=20, choices=(('desayuno', 'Desayuno'), ('almuerzo', 'Almuerzo'), ('merienda', 'Merienda'), ('cena', 'Cena')))
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    comensales = models.PositiveIntegerField(default=115)

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
    fecha_calculo = models.DateTimeField(auto_now_add=True)  # Fecha y hora en que se realizó el cálculo
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    temporada = models.CharField(max_length=20, choices=(('verano', 'Verano'), ('invierno', 'Invierno')))
    insumos = models.TextField()  # Almacenaremos los insumos como JSON

    def __str__(self):
        return f"Cálculo del {self.fecha_calculo} para {self.fecha_inicio} a {self.fecha_fin} ({self.temporada})"