from django.contrib import admin
from django.urls import path, include
from .views import agregar_producto
from . import views

urlpatterns = [
    path('productos/', views.PruebaView.as_view(), name='productos'),
    path('agregar-producto/', agregar_producto, name="agregar_producto")
]
