from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

#*******VIEWS HOME*******
class Prueba2View(TemplateView):
    template_name = 'home/prueba.html'

class PruebaView(TemplateView):
    template_name = 'home/base.html'

# class NosotrosView(TemplateView):
#     template_name = 'home/nosotros.html'

# class HomeView(TemplateView):
#     template_name = 'home/home.html'

#*******VIEWS HOME Using RENDER*******
def nosotros(request):
    return render(request, "home/nosotros.html")

def home(request):
    return render(request, "home/home.html")


#*******VIEWS LOGIN*******

def loginView(request):
    return render(request, "login.html",{
        'form': UserCreationForm
    })