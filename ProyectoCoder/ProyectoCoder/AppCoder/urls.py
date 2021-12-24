from django.urls import path
from AppCoder import views


#para el logout
from django.contrib.auth.views import LogoutView


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
    
    #PARA CLASES BASADAS EN VISTAS
    path('curso/list', views.CursoList.as_view(), name='List'),
    
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    
    
    
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    
    
    
    #Clase 23 LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
   
    
]