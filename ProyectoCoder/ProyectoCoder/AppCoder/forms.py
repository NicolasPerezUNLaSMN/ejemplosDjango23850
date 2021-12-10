from django import forms







class EstadioFormulario(forms.Form):
    
    #campos
    direccion = forms.CharField(required=True)
    anioFund  = forms.IntegerField()