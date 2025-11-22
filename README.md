# Rama: Urls_3

## Objetivo

En esta rama se ha creado la funcionalidad para mostrar todos los entrenadores cuyo nombre es "Eduardo" y cuya fecha de contratación sea en el año 2000 almacenadas en la base de datos utilizando Django.
Utilizando filtros con OR con Q objects.

---

## View utilizada

### Vista para que muestre las categorias con todos sus atributos

```python
  def mostrar_entrenadores(request, nombre, anio):
    entrenadores = Entrenador.objects.all().filter(Q(nombre=nombre) | Q(fecha_contratacion__year=anio))
    '''
    entrenadores = (Entrenador.objects.raw("SELECT * FROM club_entrenador e "
                                    + " WHERE e.nombre = 'Eduardo' "
                                    + " OR EXTRACT(YEAR FROM e.fecha_contratacion) = 2000 "))
    '''
    return render(request, 'app_club/entrenador/entrenadores.html', {"mostrar_entrenadores":entrenadores})

```

## Se ha usado el EXTRACT(YEAR FROM e.fecha_contratacion) = 2000 para filtar por año

## Template: entrenadores.html

```python
<!DOCTYPE html>
<html>
  <head>
    <title>Entrenadores</title>
  </head>
  <body>
    <h1>Entrenadores</h1>

    <table border="1" cellpadding="6">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Salario</th>
          <th>Fecha de contratación</th>
          <th>Activo</th>
        </tr>
      </thead>

      <tbody>
        {% for entrenadores in mostrar_entrenadores %}
        <tr>
          <td>{{ entrenadores.nombre }}</td>
          <td>{{ entrenadores.salario }}</td>
          <td>{{ entrenadores.fecha_contratacion }}</td>
          <td>{{ entrenadores.activo }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>


```

---

## URL configurada

path('entrenadores/<str:nombre>/<int:anio>/', views.mostrar_entrenadores, name="mostrar_entrenadores"),

### Enlace desde el index

```python
 <li>
    <a href="{% url 'mostrar_entrenadores' 'Eduardo' 2000 %}">Muestra los entrenadores con filtro OR</a>
  </li>

```

---

## Resultado

Al acceder al enlace desde la página principal, se muestra una tabla con todas las jugadores registradas en la base de datos, incluyendo:

- **Nombre**

- **Salario**

- **Feha de contratación**

- **Activo**
