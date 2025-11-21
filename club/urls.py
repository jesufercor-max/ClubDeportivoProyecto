from django.urls import path
from .import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/', views.mostrar_categorias, name="mostrar_categorias"),
]

# path('<nombre_html', views.<nombre_vista>, name=)