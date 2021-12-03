from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#Primer vista
def inicio(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')


def jugadores(request):
    
    
    return render(request, 'AppCoder/jugadores.html')