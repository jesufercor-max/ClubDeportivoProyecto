from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.mostrar_categorias, name="mostrar_categorias"),
    path('jugadores/<str:categoria_tipo>/<str:palabra_descripcion>/', views.mostrar_jugadores, name="mostrar_jugadores"),
    path('entrenadores/<str:nombre>/<int:anio>/', views.mostrar_entrenadores, name="mostrar_entrenadores"),
    path('entrenamientos/', views.mostrar_entrenamientos, name="mostrar_entrenamientos"),

]

# path('<nombre_html', views.<nombre_vista>, name=)