# Rama: Urls_2

## Objetivo

En esta rama se ha creado la funcionalidad para mostrar todos los jugadores pertenecientes
a una categoría concreta y cuya descripcion contenga "magicos" almacenadas en la base de datos utilizando Django.
Utilizando filtros con AND sobre una relación ManyToOne (Jugador → Categoria).

---

## View utilizada

### Vista para que muestre las categorias con todos sus atributos

```python
  def mostrar_jugadores(request, categoria_tipo, palabra_descripcion):
      jugadores = Jugador.objects.select_related("categoria").filter(categoria__tipos=categoria_tipo).filter(categoria__descripcion__icontains=palabra_descripcion)
      '''
      jugadores = (Jugador.objects.raw("SELECT * FROM club_Jugador j "
                                  + " INNER JOIN club_Categoria c ON j. categoria_id = c.id "
                                  + " WHERE c.tipos = 'AL' "
                                  + " AND c.descripcion LIKE '%magicos%' "))
      '''
    return render (request, 'app_club/jugador/jugadores_por_categoria.html', {"mostrar_jugadores":jugadores})
```

---

## Template: jugadores_por_categoria.html

```python
<!DOCTYPE html>
<html>
  <head>
    <title>Jugadores</title>
  </head>
  <body>
    <h1>Jugadores</h1>

    <table border="1" cellpadding="6">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Dorsal</th>
          <th>Fecha de nacimiento</th>
          <th>Categoria</th>
          <th>Descripción</th>
        </tr>
      </thead>

      <tbody>
        {% for jugadores in mostrar_jugadores %}
        <tr>
          <td>{{ jugadores.nombre }}</td>
          <td>{{ jugadores.dorsal }}</td>
          <td>{{ jugadores.fecha_nacimiento }}</td>
          <td>{{ jugadores.categoria.tipos }}</td>
          <td>{{ jugadores.categoria.descripcion }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </body>
</html>

```

---

## URL configurada

path('jugadores/<str:categoria_tipo>/<str:palabra_descripcion>/', views.mostrar_jugadores, name="mostrar_jugadores"),

### Enlace desde el index

```python
 <li>
      <a href="{% url 'mostrar_jugadores' 'AL' 'magicos' %}">
        Muestra los jugadores que pertenecen a la Categoria Alevin, y cuya
        descripcion contiene "magicos"
      </a>
  </li>

```

---

## Resultado

Al acceder al enlace desde la página principal, se muestra una tabla con todas las jugadores registradas en la base de datos, incluyendo:

- **Nombre**

- **Dorsal**

- **Feha de nacimiento**

- **Categoría**

- **Descripción**
