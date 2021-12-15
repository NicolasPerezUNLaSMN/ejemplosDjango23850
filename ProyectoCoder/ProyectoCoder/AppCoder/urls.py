from django.urls import path
from AppCoder import views


urlpatterns = [
   
    
    path('inicio', views.inicio, name="Inicio"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('estadioFormulario', views.estadioFormulario),
    path('busquedaEquipo', views.busquedaEquipo),
    path('buscar/', views.buscar),
    path('empleadoFormulario', views.empleadoFormulario),
    
    
    path('jugadorFormulario', views.jugadorFormulario, name="JugadorFormulario"),
    path('leerJugadores', views.leerJugadores, name="LeerJugadores"),
    path('eliminarJugador/<numero_para_borrar>/', views.eliminarJugador, name="EliminarJugador"),
    path('editarJugador/<numero_para_editar>/', views.editarJugador, name="EditarJugador"),
    
   
    
    
]