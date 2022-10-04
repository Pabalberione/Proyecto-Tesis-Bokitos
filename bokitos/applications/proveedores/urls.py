from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='proveedores'),
    path('proveedores/añadir_proveedor', views.añadir, name='añadir')
]
