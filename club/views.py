from django.shortcuts import render
from .models import Categoria, Jugador, Entrenador, EstadisticasJugador
from django.db.models import Q, Sum, Avg

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

# Vista que busca entrenadores utilizando un filtro OR con Q objects
# Realiza una búsqueda de entrenadores combinando varias condiciones mediante OR, como coincidencia en el nombre o años de experiencia.
# Demuestra el uso de filtros OR en QuerySet.
def mostrar_entrenadores(request, nombre, anio):
    entrenadores = Entrenador.objects.all().filter(Q(nombre=nombre) | Q(fecha_contratacion__year=anio))
    '''
    entrenadores = (Entrenador.objects.raw("SELECT * FROM club_entrenador e "
                                    + " WHERE e.nombre = 'Eduardo' "
                                    + " OR EXTRACT(YEAR FROM e.fecha_contratacion) = 2000 "))
    '''
    return render(request, 'app_club/entrenador/entrenadores.html', {"mostrar_entrenadores":entrenadores})
    
# Vista que calcula estadísticas globales del club usando aggregate()
# y calcula el total de goles, asistencias y minutos jugados.
# Utiliza la función aggregate() para obtener sumas de forma optimizada
def mostrar_estadisticas (request):
    estadisticas = EstadisticasJugador.objects.aggregate(goles_totales=Sum('goles'), asistencias_totales=Sum('asistencias'), minutos_totales=Sum('minutos_jugados'))
    media = estadisticas["goles_totales"] / estadisticas["minutos_totales"]
    '''
    estadisticas = (EstadisticasJugador.objects.raw("SELECT SUM(goles) AS goles_totales, "
                                            + " SUM(asistencias) AS asistencias_totales, "
                                            + " SUM(minutos_jugados) AS minutos_totales, "
                                            + " SUM(goles) / (SUM(minutos_jugados) AS media "
                                            + " FROM estadisticasjugador; "))
    '''
    return render (request, 'app_club/EstadisticaJugador/estadisticas.html', {"estadisticas":estadisticas, "media":media})

