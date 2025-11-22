from django.contrib import admin
from .models import Jugador,Categoria,Entrenador,Entrenamiento,Lesion,Partido,EstadisticasJugador,Plantilla,Pago,Asistencia,Participacion

# Register your models here.

admin.site.register(Jugador)
admin.site.register(Categoria)
admin.site.register(Entrenador)
admin.site.register(Entrenamiento)
admin.site.register(Lesion)
admin.site.register(Pago)
admin.site.register(Participacion)
admin.site.register(Partido)	
admin.site.register(Plantilla)
admin.site.register(EstadisticasJugador)
admin.site.register(Asistencia)

             