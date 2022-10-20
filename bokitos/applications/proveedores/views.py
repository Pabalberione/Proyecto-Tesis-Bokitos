from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from .forms import añadirProveedor
from .models import proveedor

# class PruebaView(TemplateView):
#     template_name = 'proveedores/proveedores.html'
    
def proveedores(request):
    proveedores = proveedor.objects.all()
    return render(request, 'proveedores/proveedores.html', {'proveedores':proveedores})


#---AGREGAR PROVEEDOR---
def proveedor_agregado(request):
    if request.POST:
        form = añadirProveedor(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'proveedores/proveedor_agregado.html')


def agregar_proveedor(request):
    form = añadirProveedor
    return render(request, 'proveedores/agregar_proveedor.html', {'form':form})



#---ELIMINAR PROVEEDOR---
def eliminar_proveedor(request, pk):
    proveedores = proveedor.objects.all()
    proveedor1 = proveedor.objects.get(id=pk)
    proveedor1.delete()
    return render(request, 'proveedores/proveedores.html', {'proveedores':proveedores})



#--------------------------------------------------CODIGO VIEJO  -------------------------------------------------------------------------------------------------------

#FUNCION AGREGAR PROVEEDOR VIEJA
# def agregar_proveedor(request):
#     form = añadirProveedor(request.POST, request.FILES)
#     print(request.FILES)
#     return render(request, 'proveedores/agregar_proveedor.html', {'form':form})

#CODIGO HTML AGREGADO PARA EL FORMULARIO AGREGAR PROVEEDOR
# <!-- {%block content%}
#     <form method="post" action="{% url 'proveedor_agregado' %}" enctype="multipart/form-data">
#         {% csrf_token %}
#         {{ form.as_p }} 
#         <button>Guardar</button>
#     </form>
        
            
# {%endblock%} -->


#----ELIMINAR PROVEEDOR---
# class ProveedorDeleteView(DeleteView):
#     model = proveedor
#     template_name = "proveedores/eliminar_proveedor.html"
#     success_url = reverse_lazy('proveedor_eliminado.html')