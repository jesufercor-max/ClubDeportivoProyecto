# Rama: Urls_5

## Objetivo

En esta rama se ha creado la funcionalidad para mostrar todas las estadisticas del club, cogiendo la información del total de goles, asistencias y creando una media para saber cuantos goles por minutos se generan, almacenadas en la base de datos utilizando Django.
Utilizando aggregate().

---

## View utilizada

### Vista para que muestre las categorias con todos sus atributos

```python
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


```

## Template: estadisticas.html

```python
<!DOCTYPE html>
<html>
  <head>
    <title>Estadisticas del club</title>
  </head>
  <body>
    <h1>Estadisticas del club</h1>

    <table border="1" cellpadding="6">
      <thead>
        <tr>
          <th>Total Goles</th>
          <th>Total Asistencias</th>
          <th>Total Minutos jugados</th>
          <th>Goles/minutos</th>
        </tr>
      </thead>

      <tbody>
        <tr>
            <td>{{ estadisticas.goles_totales }}</td>
            <td>{{ estadisticas.asistencias_totales }}</td>
            <td>{{ estadisticas.minutos_totales }}</td>
            <td>{{ media }}</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>

```

---

## URL configurada

path('estadisticas/', views.mostrar_estadisticas, name="mostrar_estadisticas")

### Enlace desde el index

```python
  <li>
    <a href="{% url 'mostrar_estadisticas' %}">Muestra las estadisticas del club completo</a>
  </li>

```

---

## Resultado

Al acceder al enlace desde la página principal, se muestra una tabla con todas las jugadores registradas en la base de datos, incluyendo:

- **Total Goles**

- **Total Asistencias**

- **Total Minutos jugados**

- **Goles/minutos**
