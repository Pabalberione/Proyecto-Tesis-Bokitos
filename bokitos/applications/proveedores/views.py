from django.shortcuts import redirect, render
# Create your views here.
from .forms import añadirProveedor
from .models import proveedor


# class PruebaView(TemplateView):
#     template_name = 'proveedores/proveedores.html'
    
def proveedores(request):
    proveedores = proveedor.objects.all()
    return render(request, 'proveedores/proveedores.html', {'proveedores':proveedores})

#def delete_proveedor(request, proveedor_id): #Se le agrega un ID porque para eliminar el registro hay que saber cual es el registro que se quiere eliminar 
    #print(proveedor_id)

def añadir(request):
    form = añadirProveedor(request.POST, request.FILES)
    print(request.FILES)
    return render(request, 'proveedores/añadir_proveedor.html', {'form':form})