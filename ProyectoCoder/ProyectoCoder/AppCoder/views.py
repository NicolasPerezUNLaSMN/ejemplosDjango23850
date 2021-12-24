from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.edit import CreateView

from AppCoder.models import Estadio, Equipo, Empleado, Jugador, Curso, Avatar


from AppCoder.forms import EstadioFormulario, EmpleadoFormulario, JugadorFormulario,UserRegisterForm, UserEditForm, AvatarFormulario

from django.contrib.auth.models import User


#Para el login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate



from django.contrib.auth.decorators import login_required


#CBV ---> CRUD ---> Curso



def editarJugador(request, numero_para_editar): 
    
   
    
    jugador = Jugador.objects.get(numero=numero_para_editar)
    #id, numero, nombre, esBueno
    
   
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
          
                
            #id
            jugador.apellido = informacion["apellido"]
            jugador.numero = informacion["numero"]
            jugador.esBueno = informacion["esBueno"]
              
            
            
            jugador.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = JugadorFormulario(initial={"apellido":jugador.apellido,"numero":jugador.numero,"esBueno":jugador.esBueno})
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/editarJugador.html',{"miFormulario":miFormulario,"numero_para_editar":numero_para_editar})
    
    
    


def eliminarJugador(request, numero_para_borrar):
    
    jugadorQueQuieroBorrar = Jugador.objects.get(numero=numero_para_borrar)
    jugadorQueQuieroBorrar.delete()
    
    
    jugadores = Jugador.objects.all()
    
    return render(request, "AppCoder/leerJugadores.html", {"jugadores":jugadores} )
    
    

@login_required
def leerJugadores(request):
    
    jugadores = Jugador.objects.all()
    
    dir = {"jugadores":jugadores} #contexto
    
    return render(request, "AppCoder/leerJugadores.html", dir)
    
    




def busquedaEquipo(request):
    
    return render(request, 'AppCoder/busquedaEquipo.html')


def buscar(request):
    
    
    if request.GET["nombre"]:
        
        nombre = request.GET["nombre"]
        
        equipos = Equipo.objects.filter(nombre__icontains=nombre)
        
        
        #respuesta = f"ESTOY BUSCANDO A: {request.GET['nombre']}"
        
        return render(request, "AppCoder/resultadoBusqueda.html",{"equipos":equipos, "nombre":nombre})
         
         
    else: 
        
        respuesta = "Che, mandame información"     
    
    return HttpResponse(respuesta)




# Create your views here.

def estadioFormulario(request):
    
    #obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = EstadioFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
            estadioInsta = Estadio( direccion=informacion["direccion"] , anioFund=informacion["anioFund"])
            
            estadioInsta.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = EstadioFormulario()
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/estadioFormulario.html',{"miFormulario":miFormulario})




def empleadoFormulario(request):
    
    #obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = EmpleadoFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
            emple = Empleado(
                
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                dni = informacion["dni"],
                profesional = informacion["profesional"],
                fechaDeNacimiento = informacion["fechaDeNacimiento"]
                
                
                
            )
            
            emple.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = EmpleadoFormulario()
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/empleadoFormulario.html',{"miFormulario":miFormulario})



def jugadorFormulario(request):
    
    #obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = JugadorFormulario(request.POST)
        
        if miFormulario.is_valid():  #va con ()
            
            informacion = miFormulario.cleaned_data
        
            juga = Jugador(
                
                apellido = informacion["apellido"],
                numero = informacion["numero"],
                esBueno = informacion["esBueno"]
              
                
                
                
            )
            
            juga.save() #Es el que guarda en la BD
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = JugadorFormulario()
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/jugadorFormulario.html',{"miFormulario":miFormulario})








#Primer vista
def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url 
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html', diccionario)


def jugadores(request):
    
    
    return render(request, 'AppCoder/jugadores.html')


def equipos(request):
    
    
    return render(request, 'AppCoder/equipos.html')



from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy

#Leer --- nos da todos los cursos
class CursoList(ListView):
    
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class CursoDetalle(DetailView):
    
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
#Crear elementos
class CursoCreacion(CreateView):
    
    model = Curso
    success_url = "../curso/list"  #AppCoder/template/AppCoder/editar
    fields = ["nombre", "camada", "esNoche"]
    
#modificar!!!!!!!!!!!  
class CursoUpdate(UpdateView):
    
    model = Curso
    success_url = "../curso/list"
    fields = ["nombre", "camada", "esNoche"]
  
#Borrar   
class CursoDelete(DeleteView):
    
    model = Curso
    success_url = "../curso/list"
    
    


def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"DATOS MALOS :(!!!!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"FORMULARIO erroneo"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )



def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Creado :)"})


      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})
  
  
  
  
@login_required
def editarPerfil(request):
    
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})




@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})
