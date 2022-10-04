from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.
from django.views.generic.base import TemplateView


class PruebaView(TemplateView):
    template_name = 'productos/productos.html'

def agregar_producto(request):
    return render (request, 'productos/agregar.html')
