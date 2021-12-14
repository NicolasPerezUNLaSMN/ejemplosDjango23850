from django import forms
import datetime


class EmpleadoFormulario(forms.Form):
    
    #Campos queremos que se vean en la web
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    profesional = forms.BooleanField()
    fechaDeNacimiento = forms.DateField(initial=datetime.date.today)





class EstadioFormulario(forms.Form):
    
    #campos
    direccion = forms.CharField(required=True)
    anioFund  = forms.IntegerField()
    
    
