from django.shortcuts import render
from .models import Categoria, Jugador

# Create your views here.

# Vista de la página principal donde van a estar todas las urls
def index(request):
    return render (request, 'index.html')

# Vista para que muestre las categorias con todos sus atributos
def mostrar_categorias(request):
    categorias = Categoria.objects.all()
    '''
    categorias = (Categoria.objects.raw("SELECT * FROM club_Categoria"))
    '''
    return render(request, 'app_club/categoria/categorias.html', {"mostrar_categorias":categorias})

# Vista para mostrar jugadores filtrados por categoría usando un filtro AND
# Muestra todos los jugadores pertenecientes 
# a una categoría concreta y cuya descripcion contenga "magicos"
# Utiliza filtros con AND sobre una relación ManyToOne (Jugador → Categoria).
def mostrar_jugadores(request, categoria_tipo, palabra_descripcion):
    jugadores = Jugador.objects.select_related("categoria").filter(categoria__tipos=categoria_tipo).filter(categoria__descripcion__icontains=palabra_descripcion)
    '''
    jugadores = (Jugador.objects.raw("SELECT * FROM club_Jugador j "
                                + " INNER JOIN club_Categoria c ON j.categoria_id = c.id "
                                + " WHERE c.tipos = 'AL' "
                                + " AND c.descripcion LIKE '%magicos%' "))
    '''
    return render (request, 'app_club/jugador/jugadores_por_categoria.html', {"mostrar_jugadores":jugadores})

