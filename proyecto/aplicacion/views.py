from django.shortcuts import render,redirect
from .models import Medico, Paciente, Turno, Avatar, Empleado
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import MedicoForm
from .forms import PacienteForm
from .forms import TurnoForm
from .forms import RegistroUsuariosForm
from.forms import UserEditForm
from .forms import AvatarFormulario

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



def home (request):
    return render(request, "aplicacion/home.html")


@login_required
def medicos (request):
    contexto = {'medicos' : Medico.objects.all(), 'titulo' : 'Reporte de Medicos', 'grupos' : ['32332' , '87687']}
    return render(request, "aplicacion/medicos.html", contexto)

@login_required
def pacientes (request):
    contexto = {'pacientes' : Paciente.objects.all()}
    return render(request, "aplicacion/pacientes.html" , contexto)
@login_required
def turnos (request):
    contexto = {'turnos' : Turno.objects.all()}
    return render(request, "aplicacion/turnos.html" , contexto)

@login_required
def empleados (request):
    contexto = {'empleados' : Empleado.objects.all()}
    return render(request, "aplicacion/empleados.html" , contexto)

def info (request):
    return render(request, "aplicacion/info.html")

@login_required
def medicoForm(request):
    if request.method == "POST":
        medico = Medico(nombre=request.POST['nombre'],
                        dni=request.POST['dni'])
        medico.save()
        return HttpResponse("Se grabo con exito el medico!")
    return render(request, "aplicacion/medicoForm.html")

@login_required
def medicoForm2(request):
    if request.method == "POST":
        miForm = MedicoForm(request.POST)
        if miForm.is_valid():
            medico_nombre = miForm.cleaned_data.get('nombre')
            medico_dni = miForm.cleaned_data.get('dni')
            medico = Medico(nombre=medico_nombre , dni = medico_dni)
            medico.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = MedicoForm()
    
    return render(request, "aplicacion/medicoForm2.html", {"form" : miForm})


@login_required
def buscarMedico(request):
    return render(request,"aplicacion/buscarMedico.html")
@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        medicos = Medico.objects.filter(nombre__icontains=patron)
        contexto = {"medicos" : medicos,'titulo' : f'Reporte de Medicos que tiene "{patron}"'}
        return render(request, "aplicacion/medicos.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")
@login_required
def pacienteForm(request):
    if request.method == "POST":
        paciente = Paciente(nombre=request.POST['nombre'],
                        dni=request.POST['dni'],
                        apellido=request.POST['apellido'],
                        edad=request.POST['edad'])
        
        paciente.save()
        return HttpResponse("Se grabo con exito el paciente!")
    return render(request, "aplicacion/pacienteForm.html")
@login_required
def pacienteForm2(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get('nombre')
            paciente_apellido = miForm.cleaned_data.get('apellido')
            paciente_edad = miForm.cleaned_data.get('edad')
            paciente_dni = miForm.cleaned_data.get('dni')
            paciente = Paciente(nombre = paciente_nombre, dni = paciente_dni, apellido = paciente_apellido , edad = paciente_edad)
            paciente.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = PacienteForm()
    
    return render(request, "aplicacion/pacienteForm2.html", {"form" : miForm})

@login_required
def turnoForm(request):
    if request.method == "POST":
        turno = Turno(nombre=request.POST['nombre'],
                        dni=request.POST['dni'],
                        fecha=request.POST['fecha'])
        turno.save()
        return HttpResponse("Se grabo con exito el turno!")
    return render(request, "aplicacion/turnoForm.html")

@login_required
def turnoForm2(request):
    if request.method == "POST":
        miForm = TurnoForm(request.POST)
        if miForm.is_valid():
            turno_nombre = miForm.cleaned_data.get('nombre')
            turno_dni = miForm.cleaned_data.get('dni')
            turno_fecha = miForm.cleaned_data.get('fecha')
            turno = Turno(nombre=turno_nombre , dni = turno_dni,  fecha = turno_fecha)
            turno.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = TurnoForm()
    
    return render(request, "aplicacion/turnoForm2.html", {"form" : miForm})


@login_required
def EmpleadoForm(request):
    if request.method == "POST":
        empleado = Empleado(nombre=request.POST['nombre'],
                        apellido=request.POST['apellido'],
                        edad=request.POST['edad'],
                        trabajo=request.POST['trabajo'],
                        sueldo=request.POST['sueldo'],
                        )
        empleado.save()
        return HttpResponse("Se grabo con exito el empleado!")
    return render(request, "aplicacion/empleadoForm.html")

@login_required
def empleadoForm2(request):
    if request.method == "POST":
        miForm = EmpleadoForm(request.POST)
        if miForm.is_valid():
            empleado_nombre = miForm.cleaned_data.get('nombre')
            empleado_apellido = miForm.cleaned_data.get('apellido')
            empleado_edad = miForm.cleaned_data.get('edad')
            empleado_trabajo = miForm.cleaned_data.get('trabajo')
            empleado_sueldo = miForm.cleaned_data.get('sueldo')
            empleado = Empleado(nombre=empleado_nombre , apellido = empleado_apellido, edad = empleado_edad, trabajo = empleado_trabajo, sueldo = empleado_sueldo )
            empleado.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = EmpleadoForm()
    
    return render(request, "aplicacion/empleadoForm2.html", {"form" : miForm})



@login_required
def updatePaciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            paciente.nombre = miForm.cleaned_data.get('nombre')
            paciente.dni = miForm.cleaned_data.get('dni')
            paciente.apellido = miForm.cleaned_data.get('apellido')
            paciente.edad = miForm.cleaned_data.get('edad')
            paciente.save()
            return redirect(reverse_lazy('pacientes'))
    else:
        miForm = PacienteForm(initial={
            'nombre' : paciente.nombre,
            'dni' : paciente.dni,
            'apellido' : paciente.apellido,         
            'edad' : paciente.edad, 
        })
    return render(request, "aplicacion/pacienteForm.html" , {'form' : miForm})

@login_required
def deletePaciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()
    return redirect(reverse_lazy('pacientes'))

@login_required
def createPaciente(request):
    if request.method == "POST":
        miForm = PacienteForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_dni = miForm.cleaned_data.get('dni')
            p_apellido = miForm.cleaned_data.get('apellido')
            p_edad = miForm.cleaned_data.get('edad')

            paciente = Paciente(nombre=p_nombre,
                                apellido=p_apellido,
                                dni=p_dni, edad=p_edad)
            paciente.save()
            return redirect(reverse_lazy('pacientes'))
    else:
        miForm = PacienteForm()
    return render(request, "aplicacion/pacienteForm.html" , {'form' : miForm})




class TurnoList(LoginRequiredMixin, ListView):
    model = Turno

class TurnoCreate(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ['nombre' , 'dni' , 'fecha']
    success_url = reverse_lazy('turnos')
    
class TurnoUpdate(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ['nombre' , 'dni' , 'fecha']
    success_url = reverse_lazy('turnos')

class TurnoDelete(LoginRequiredMixin, DeleteView):
    model = Turno
    fields = ['nombre' , 'dni' , 'fecha']
    success_url = reverse_lazy('turnos')

class MedicoList(LoginRequiredMixin, ListView):
    model = Medico

class MedicoCreate(LoginRequiredMixin, CreateView):
    model = Medico
    fields = ['nombre' , 'apellido' , 'dni' , 'especialidad' ]
    success_url = reverse_lazy('medicos')
    
class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = Medico
    fields = ['nombre' , 'apellido' , 'dni' , 'especialidad' ]
    success_url = reverse_lazy('medicos')

class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = Medico
    fields = ['nombre' , 'apellido' , 'dni' , 'especialidad' ]
    success_url = reverse_lazy('medicos')

class EmpleadoList(LoginRequiredMixin, ListView):
    model = Empleado

class EmpleadoCreate(LoginRequiredMixin, CreateView):
    model = Empleado
    fields = ['nombre' , 'apellido' , 'edad' ,'trabajo' , 'sueldo']
    success_url = reverse_lazy('empleados')
    
class EmpleadoUpdate(LoginRequiredMixin, UpdateView):
    model = Empleado
    fields = ['nombre' , 'apellido' , 'edad' ,'trabajo' , 'sueldo']
    success_url = reverse_lazy('empleados')

class EmpleadoDelete(LoginRequiredMixin, DeleteView):
    model = Empleado
    fields = ['nombre' , 'apellido' , 'edad' ,'trabajo' , 'sueldo']
    success_url = reverse_lazy('empleados')


#_______________ Login / Logout / Registracion 


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.jpg"
                finally:
                    request.session["avatar"] = avatar

                return redirect('home') 

            else:
                messages.error(request, 'Usuario o contraseña son inválidos')
                return render(request, "aplicacion/login.html", {'form': miForm})

        else:
            messages.error(request, 'Usuario o contraseña son inválidos')
            return render(request, "aplicacion/login.html", {'form': miForm})

    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {'form': miForm})

@login_required
def welcome_view(request):
    messages.success(request, f'Bienvenido al Sitio web {request.user.username}')
    
    try:
        avatar = Avatar.objects.get(user=request.user.id).imagen.url
    except:
        avatar = "/media/avatares/default.jpg"
    finally:
        request.session["avatar"] = avatar
    
    return render(request, "aplicacion/base.html", {'msj': f'Bienvenido al Sitio web {request.user.username}'})

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            messages.success(request, f'Registro exitoso para el usuario {usuario}. ¡Inicia sesión ahora!')
            return redirect('login')
    else: 
        miForm = RegistroUsuariosForm()

    
    return render(request, "aplicacion/registro.html", {'form': miForm})




@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('editar_perfil')  
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user = u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request, "aplicacion/base.html" )
        
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form' : form})

