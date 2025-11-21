# Rama: Urls_1
## Objetivo

En esta rama se ha creado la funcionalidad para mostrar todas las categorías almacenadas en la base de datos utilizando Django.

---

## View utilizada
### Vista para que muestre las categorias con todos sus atributos
```python
  def mostrar_categorias(request):
      categorias = Categoria.objects.all()
      '''
      categorias = (Categoria.objects.raw("SELECT * FROM Categorias"))
      '''
      return render(request, 'app_club/categorias.html', {"mostrar_categorias":categorias})
```
---

## Template: categorias.html
```python
<!DOCTYPE html>
  <html>
    <head>
        <title>Categorías</title>
    </head>
    <body>

      <h1>Categorías</h1>

      <table border="1" cellpadding="6">
          <thead>
              <tr>
                  <th>Tipo</th>
                  <th>Descripción</th>
                  <th>Edad mínima</th>
                  <th>Edad máxima</th>
              </tr>
          </thead>

          <tbody>
          {% for categorias in mostrar_categorias %}
              <tr>
                  <td>{{ categorias.tipos }}</td>
                  <td>{{ categorias.descripcion }}</td>
                  <td>{{ categorias.edad_min }}</td>
                  <td>{{ categorias.edad_max }}</td>
              </tr>
          {% endfor %}
          </tbody>
      </table>

    </body>
  </html>

```
---

## URL configurada
path('categorias/', views.mostrar_categorias, name="mostrar_categorias"),

### Enlace desde el index
```python
<li><a href="{% url 'mostrar_categorias' %}">Muestra las categorias</a></li>

```
---

## Resultado

Al acceder al enlace desde la página principal, se muestra una tabla con todas las categorías registradas en la base de datos, incluyendo:

- **Tipo**

- **Descripción**

- **Edad mínima**

- **Edad máxima**