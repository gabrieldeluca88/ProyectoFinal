from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-auto', agregar_auto, name="AgregarAuto"),
    path('l-autos', lista_autos, name="ListaAutos"),
    path('el-autos/<int:id>', eliminar_auto, name="EliminarAuto"),
    path('ed-autos/<int:id>', editar_auto, name="EditarAuto"),
    path('ag-resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
    path('busq-auto', busqueda_autos, name="BusquedaAutos"),
    path('buscar-modelo', buscar_modelo, name="BuscarModelo"),
    path('buscar-tipo', buscar_tipo, name="BuscarTipo"),
    path('buscar-marca', buscar_marca, name="BuscarMarca"),
    path('buscar-valoracion', buscar_valoracion, name="BuscarValoracion"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_temas, name='Foro'),
    path('crear-tema', crear_tema, name='CrearTema'),
    path('ed-tema/<int:pk>', editar_tema, name='EditarTema'),
    path('el-tema/<int:pk>', eliminar_tema, name='EliminarTema'),
    path('foro/<int:pk>/', detalle_tema, name='DetalleTema'),
    path('<int:pk>/crear-coment', crear_comentario, name='CrearComentario'),
]