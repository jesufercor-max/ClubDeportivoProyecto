from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.utils import timezone

from club.models import (
    Categoria, Entrenador, Jugador, Entrenamiento, Lesion,
    Partido, EstadisticasJugador, Plantilla, Pago,
    Asistencia, Participacion
)

class Command(BaseCommand):
    help = "Generando datos usando Faker"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # -----------------------
        # 1. CATEGORIAS (10)
        # -----------------------
        categorias = []
        for _ in range(10):
            cat = Categoria.objects.create(
                tipos=random.choice(["PRE", "BEM", "AL", "IN", "CA", "JU"]),
                descripcion=fake.text(),
                edad_min=random.randint(6, 14),
                edad_max=random.randint(15, 18),
            )
            categorias.append(cat)

        # -----------------------
        # 2. ENTRENADORES (10)
        # -----------------------
        entrenadores = []
        for categoria in categorias[:10]:  # aseguramos OneToOne único
            ent = Entrenador.objects.create(
                nombre=fake.name(),
                salario=random.uniform(400, 1200),
                fecha_contratacion=fake.date_between(start_date="-3y", end_date="today"),
                activo=random.choice([True, False]),
                categoria=categoria  # OneToOne
            )
            entrenadores.append(ent)

        # -----------------------
        # 3. JUGADORES (10)
        # -----------------------
        jugadores = []
        for _ in range(10):
            jug = Jugador.objects.create(
                nombre=fake.name(),
                dorsal=random.randint(1, 99),
                fecha_nacimiento=fake.date_between(start_date="-17y", end_date="-6y"),
                categoria=random.choice(categorias),
                entrenador=random.choice(entrenadores),
            )
            jugadores.append(jug)

        # -----------------------
        # 4. ENTRENAMIENTOS (10)
        # -----------------------
        entrenamientos = []
        for _ in range(10):
            ent = Entrenamiento.objects.create(
                horario_entrenamiento=fake.date_time_this_year(),
                duracion_minutos=random.randint(45, 120),
                categoria=random.choice(categorias),
                entrenador=random.choice(entrenadores),
            )
            entrenamientos.append(ent)

        # -----------------------
        # 5. PARTIDOS (10)
        # -----------------------
        partidos = []
        for _ in range(10):
            p = Partido.objects.create(
                equipo_local=fake.city(),
                equipo_visitante=fake.city(),
                fecha=fake.date_time_this_year(),
                lugar=fake.address(),
                goles_local=random.randint(0, 7),
                goles_visitante=random.randint(0, 7),
            )
            partidos.append(p)

        # -----------------------
        # 6. ESTADISTICAS (10)
        # -----------------------
        estadisticas = []
        jugadores_1a1 = jugadores.copy()
        random.shuffle(jugadores_1a1)

        for jugador in jugadores_1a1[:10]:  # OneToOne
            e = EstadisticasJugador.objects.create(
                goles=random.randint(0, 7),
                asistencias=random.randint(0, 5),
                minutos_jugados=random.randint(0, 90),
                jugador=jugador,
                partido=random.choice(partidos),
            )
            estadisticas.append(e)

        # -----------------------
        # 7. PLANTILLAS (10)
        # -----------------------
        plantillas = []
        for _ in range(10):
            pl = Plantilla.objects.create(
                temporada=str(fake.year()),
                categoria=random.choice(categorias),
                entrenador=random.choice(entrenadores),
            )
            pl.jugadores.set(random.sample(jugadores, random.randint(4, 10)))
            plantillas.append(pl)

        # -----------------------
        # 8. PAGOS (10)
        # -----------------------
        for _ in range(10):
            Pago.objects.create(
                concepto=random.choice(["Mensualidad", "Material", "Viaje"]),
                monto=round(random.uniform(10, 100), 2),
                pagado=random.choice([True, False]),
                fecha_pago=fake.date_time_this_year(),
                jugador=random.choice(jugadores),
            )

        # -----------------------
        # 9. ASISTENCIAS (10)
        # -----------------------
        for _ in range(10):
            Asistencia.objects.create(
                entrenamiento=random.choice(entrenamientos),
                jugador=random.choice(jugadores),
                presente=random.choice([True, False]),
                observaciones=fake.text(),
            )

        # -----------------------
        # 10. PARTICIPACIONES (10)
        # -----------------------
        for _ in range(10):
            Participacion.objects.create(
                jugador=random.choice(jugadores),
                partido=random.choice(partidos),
                minutos_jugados=random.randint(0, 90),
                titular=random.choice([True, False]),
                goles=random.randint(0, 3),
            )

       
        # -----------------------
        # 11. LESIONES (10)
        # -----------------------
        lesiones = []
        self.stdout.write(f"Jugadores: {len(jugadores)}, Entrenamientos: {len(entrenamientos)}")
        for _ in range(10):
            jugador = random.choice(jugadores)
            
            # Evitar duplicar jugador en OneToOneField
            if Lesion.objects.filter(jugador=jugador).exists():
                continue  # saltamos si ya tiene lesión
            
            entrenamiento = random.choice(entrenamientos)
            entrenador = entrenamiento.entrenador  # coger entrenador del entrenamiento
            
            lesion = Lesion.objects.create(
                tipo=random.choice(["Esguince", "Fractura", "Contractura", "Corte"]),
                fecha=fake.date_time_this_year(),
                descripcion=fake.text(max_nb_chars=100),
                jugador=jugador,
                entrenamiento=entrenamiento,
                entrenador=entrenador
            )
            lesiones.append(lesion)
        self.stdout.write(self.style.SUCCESS("✓ Datos generados correctamente"))