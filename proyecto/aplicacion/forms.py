from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MedicoForm(forms.Form):
    nombre  = forms.CharField(label= "Nombre" , max_length=50, required=True)
    apellido  = forms.CharField(label= "Apellido" , max_length=50, required=True)
    dni = forms.IntegerField(label= "Dni" ,required=True)
    especialidad  = forms.CharField(label= "Especialidad" , max_length=50, required=True)

class PacienteForm(forms.Form):
    nombre  = forms.CharField(label="Nombre" , max_length=50, required=True)
    dni = forms.IntegerField(label="Dni" ,required=True)   
    apellido = forms.CharField(label="Apellido" ,max_length=50)
    edad = forms.IntegerField(label="Edad" ,required=True) 

class TurnoForm(forms.Form):
    nombre  = forms.CharField(label= "Nombre" ,max_length=50, required=True)
    dni = forms.IntegerField(label= "Dni" ,required=True)   
    fecha = forms.CharField(label= "Fecha" ,max_length=50, required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usario")
    password1 = forms.CharField(label = "Contraseña" , widget= forms.PasswordInput)
    password2 = forms.CharField(label = " Confirmar contraseña" , widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email', 'password1' , 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usario")
    password1 = forms.CharField(label = "Contraseña" , widget= forms.PasswordInput, required=True)
    password2 = forms.CharField(label = " Confirmar contraseña" , widget= forms.PasswordInput, required=True)
    primernombre = forms.CharField(label = "Nombre" , max_length=50, required=False)
    apellido = forms.CharField(label="Apellido" , max_length=50, required=False)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2', 'primernombre' , 'apellido']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

class EmpleadoForm(forms.Form):
    nombre  = forms.CharField(label="Nombre" , max_length=50, required=True)
    edad = forms.IntegerField(label="Edad" ,required=True)   
    apellido = forms.CharField(label="Apellido" ,max_length=50)
    sueldo = forms.IntegerField(label="Sueldo" ,required=True)
    trabajo  = forms.CharField(label="Trabajo" , max_length=50, required=True)


