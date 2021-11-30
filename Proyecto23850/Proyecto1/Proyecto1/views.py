from django.http import HttpResponse
from datetime import datetime

from django.template import Template, Context

def saludo(request):
	return HttpResponse("Soy Nico - Hola Django - Coder")


def segundaVista(request):
    
    
    return HttpResponse("<br><br>----------YA SOMOS PROGRAMADORES WEB----------")

def dia(request):
    
    variable = datetime.now()
    
    return HttpResponse(f"Hoy es un gran día<br>{variable}")


def apellido(request, ape):
    
    fecha = datetime.now()
    return HttpResponse(f"El profe de coder {ape}, es muy bueno..<br><br>..Por lo menos hoy:{fecha}")


def cuantosAniosTengo(request, nac):
    
    #calcular la edad --- edad
    
    return HttpResponse("TU edad es: ")


def probandoTemplate(request):
    
    miHTML = open("C:/Users/nico_/Desktop/Proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")
    
    plantilla = Template(miHTML.read())
    
    miHTML.close()
    
    miContexto = Context()  
    
    documento = plantilla.render(miContexto)
    
    return HttpResponse(documento)