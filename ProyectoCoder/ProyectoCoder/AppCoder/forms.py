from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserEditForm(UserCreationForm):

    #Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
  
 
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        
     
    
    #class Meta:
     #   model = User
     #   fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
      #  help_texts = {k:"" for k in fields}






class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
   
    #imagen_avatar = forms.ImageField(required=False)

   
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
     
    
    #class Meta:
     #   model = User
     #   fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
      #  help_texts = {k:"" for k in fields}




class JugadorFormulario(forms.Form):
    
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()
    
    
    

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
    
    
class AvatarFormulario(forms.Form):

    #Especificar los campos
    
    imagen = forms.ImageField(required=True)