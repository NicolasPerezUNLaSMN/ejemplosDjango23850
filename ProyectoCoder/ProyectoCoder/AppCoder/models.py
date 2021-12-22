from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    esNoche = models.BooleanField(null=True)
    
    def __str__(self):
        
        return f"CURSO: {self.nombre} CAMADA: {self.camada} NOCHE: {self.esNoche}"
    
   
    
class Jugador(models.Model):
    
    apellido = models.CharField(max_length=40)
    numero = models.IntegerField()
    esBueno = models.BooleanField()
    
    def __str__(self):
        
        return f"{self.apellido}, {self.numero} , {self.esBueno}"
    
    
class Equipo(models.Model):
    
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    
    
class Estadio(models.Model):
    
    direccion = models.CharField(max_length=40)
    anioFund = models.IntegerField()
    
    

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    profesional = models.BooleanField()
    fechaDeNacimiento = models.DateField()
    
    def __str__(self):
        return f"NOMBRE y APELLIDO: {self.nombre} {self.apellido}  ---- DNI: {self.dni}"
