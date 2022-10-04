from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('prueba2/', views.Prueba2View.as_view(), name='prueba2'),
    path('prueba/', views.PruebaView.as_view(), name='prueba'),
    path('login/', views.loginView, name='login'),
    #path with render home and nosotros
    path('nosotros/', views.nosotros, name='nosotros'),
    path('home/', views.home, name='home'),





]
