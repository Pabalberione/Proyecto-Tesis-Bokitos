from django.contrib import admin
from django.urls import path, include
from django import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('applications.proveedores.urls')),
    path('',include('applications.productos.urls')),
    path('',include('applications.home.urls')),
]
