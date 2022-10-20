from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from django.views.generic.base import TemplateView
from .models import producto


class PruebaView(TemplateView):
    template_name = 'productos/productos.html'

def agregar_producto(request):
    return render (request, 'productos/agregar.html')

#---PANTALLA MOSTRAR PROVEEDORES---
def productos(request):
    productos = producto.objects.all()
    return render(request, 'productos/productos.html', {'productos':productos})
