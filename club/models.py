from django.db import models
from django.utils import timezone
# Create your models here.


# -----------------------
# MODELO CATEGORIA
# -----------------------

class Categoria (models.Model):
    CATEGORIAS = [
        ('PRE', 'Prebenjamín'),
        ('BEM', 'Benjamín'),
        ('AL', 'Alevín'),
        ('IN', 'Infantil'),
        ('CA', 'Cadete'),
        ('JU', 'Juvenil'),
    ]

    tipos = model.CharField(
        max_lenght = 3,
        choises = CATEGORIAS,
        default = "AL",
    )
    descripcion = models.TextField(blank=True)
    edad_min = models.IntegerField(default=6)
    edad_max = models.IntegerField(default=18)

# -----------------------
# MODELO ENTRENADOR
# -----------------------

class Entrenador (models.Model):
    nombre = models.CharField(max_lenght = 100)
    salario = models.FloatField(default = 400.50, db_cloumn = "salario_entrenador")
    fecha_contratacion = models.DateField(default=timezone.now)
    activo = models.BooleanField(default=True)
    
    # Relaciones
    # Categoria a la que pertenece cada entrenador (One to One)
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE, related_name='entrenador')

# -----------------------
# MODELO JUGADOR
# -----------------------

class Jugador (models.Model):
    nombre = models.CharField (max_lenght = 100)
    dorsal = models.IntegerField (null=True)
    fecha_nacimiento = models.DateField()

    # Relaciones 
    # Categoria en la que juega cada jugador (ManyToOne)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='jugadores')

    # Entrenador que entrena a cada jugador (ManyToOne)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True, related_name='jugadores')

# -----------------------
# MODELO ENTRENAMIENTO
# -----------------------

class Entrenamiento (models.Model):
    horario_entrenamiento = models.DateTimeField(default=timezone.now)
    duracion_minutos = models.PositiveIntegerField(default=60)
    
    # Relaciones
    # Categoria que entrena ese dia a esa hora (ManyToOne)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Entrenador que trabaja ese dia a esa hora (ManyToOne)
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)

    # Jugadores que entrenan ese dia a esa hora (ManyToMany)
    jugadores = models.ManyToManyField(Jugador, through='Asistencia')

# -----------------------
# MODELO LESION
# -----------------------

class Lesion (models.Model):
    tipo = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=null)
    descripcion = models.TextField(max_length=250)

    # Relaciones
    # En que entrenamiento ocurrió (coge el horario del entrenamiento y la id del mismo)
    entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE)

    # Jugador que se lesiono (One to One)
    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)
    
    # Nombre del entrenador que estaba en ese entrenamiento
    entrenador = models.ForeignKey(Entrenador)

# -----------------------
# MODELO PARTIDO
# -----------------------

class Partido (models.Model):
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    lugar = models.CharField(max_length=150)
    goles_local = models.PositiveIntegerField(default=0)
    goles_visitante = models.PositiveIntegerField(default=0)
    
    # Relaciones
    # Jugadores del club que jugaron el partido
    jugadores = models.ManyToManyField(Jugador, through='Participacion')

# -----------------------
# MODELO ESTADISTICAS DEL JUGADOR
# -----------------------

class EstadisticasJugador (models.Model):
    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    minutos_jugados = models.PositiveIntegerField(default=0)

    # Relaciones
    # Jugador para sus caracteristicas
    jugador = models.OneToOneField(Jugador, on_delete=models.CASCADE)

    # Partido donde se consiguio
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)

# -----------------------
# MODELO PLANTILLA
# -----------------------

class Plantilla (models.Model):
    temporada = models.CharField(max_length=20)
    
    # Relaciones
    # Categoria a la que pertenece
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # Jugadores de la plantilla
    jugadores = models.ManyToManyField(Jugador)

    # Entrenador que entrena a esa plantilla
    entrenador = models.ForeignKey(Entrenador, on_delete=models.SET_NULL, null=True)

# -----------------------
# MODELO PAGO
# -----------------------

class Pago (models.Model):
    concepto = models.CharField(max_length=100)
    monto = models.FloatField()
    pagado = models.BooleanField(default=True)
    fecha_pago = models.DateTimeField(default=timezone.now)

    # Relaciones
    # Jugador que paga el monto
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)

# -----------------------
# MODELO INTERMEDIO: Asistencia (para ManyToMany entre Entrenamiento y Jugador)
# -----------------------

class Asistencia(models.Model):
    presente = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    # Relaciones
    # Entrenamiento al que el jugador asistio que asistió
    entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE)
    
    # Jugador que asistió
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
