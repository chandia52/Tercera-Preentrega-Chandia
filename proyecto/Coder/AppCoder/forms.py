from django import forms

class GuitarraFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   precio = forms.IntegerField(required=True)
   descripcion = forms.CharField(required=True,max_length=500)
   disponibilidad = forms.BooleanField()

class BajoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   precio = forms.IntegerField(required=True)
   descripcion = forms.CharField(required=True,max_length=500)
   disponibilidad = forms.BooleanField()

class MicrofonoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   precio = forms.IntegerField(required=True)
   descripcion = forms.CharField(required=True,max_length=500)
   disponibilidad = forms.BooleanField()

class BateriaFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   precio = forms.IntegerField(required=True)
   descripcion = forms.CharField(required=True,max_length=500)
   disponibilidad = forms.BooleanField()

