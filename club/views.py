from django.shortcuts import render
from .models import Categoria

# Create your views here.

# Vista de la página principal donde van a estar todas las urls
def index(request):
    return render (request, 'index.html')

# Vista para que muestre las categorias con todos sus atributos
def mostrar_categorias(request):
    categorias = Categoria.objects.all()
    '''
    categorias = (Categoria.objects.raw("SELECT * FROM Categorias"))
    '''
    return render(request, 'app_club/categoria/categorias.html', {"mostrar_categorias":categorias})