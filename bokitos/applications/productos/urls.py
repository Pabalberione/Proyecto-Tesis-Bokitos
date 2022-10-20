from django.contrib import admin
from django.urls import path, include
from .views import productos
from . import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('agregar-producto/', views.agregar_producto, name="agregar_producto")
]
