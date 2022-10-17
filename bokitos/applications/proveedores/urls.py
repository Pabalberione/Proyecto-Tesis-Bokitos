from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/agregar_proveedor', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/proveedor_agregado', views.proveedor_agregado, name='proveedor_agregado'),
    #path('proveedores/eliminar_proveedor/<proveedor_id>', views.eliminar_proveedor, name='eliminar-proveedor'),

]
