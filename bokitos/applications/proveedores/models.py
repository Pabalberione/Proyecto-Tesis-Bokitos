
from tkinter import CASCADE
from django.db import models

# Create your models here.
class proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    codigo_postal = models.CharField(max_length=5)
    email = models.EmailField(max_length=254)

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + "Direccion: " + self.direccion
        return fila

class productoxproveedor(models.Model):
    proveedor_id = models.ForeignKey('proveedor',on_delete=models.CASCADE)
    detalle = models.CharField(max_length=50, blank=False, null=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.detalle



