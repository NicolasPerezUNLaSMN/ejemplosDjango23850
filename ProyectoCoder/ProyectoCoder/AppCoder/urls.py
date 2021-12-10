from django.urls import path
from AppCoder import views


urlpatterns = [
   
    
    path('inicio', views.inicio, name="Inicio"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('equipos', views.equipos, name="Equipos"),
    path('estadioFormulario', views.estadioFormulario),
    path('busquedaEquipo', views.busquedaEquipo),
    path('buscar/', views.buscar),
    
    
]