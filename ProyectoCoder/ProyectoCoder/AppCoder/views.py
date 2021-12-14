from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Estadio, Equipo, Empleado


from AppCoder.forms import EstadioFormulario, EmpleadoFormulario




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
        
            estadioInsta = Estadio(direccion=informacion["direccion"] ,anioFund= informacion["anioFund"])
            
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








#Primer vista
def inicio(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')


def jugadores(request):
    
    
    return render(request, 'AppCoder/jugadores.html')


def equipos(request):
    
    
    return render(request, 'AppCoder/equipos.html')