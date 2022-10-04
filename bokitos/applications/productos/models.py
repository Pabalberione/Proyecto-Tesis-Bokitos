from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class producto(models.Model):
    descripcion = models.CharField(max_length=50, blank=False, null=False)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to="imagenes", max_length=100)
    def __str__(self):
        return self.descripcion

class stock(models.Model):
    producto_id = models.ForeignKey('producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cantidad_minima = models.IntegerField()
    def __str__(self):
        return self.cantidad, self.cantidad_minima