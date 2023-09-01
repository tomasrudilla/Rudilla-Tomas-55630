from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('medicos/', medicos, name="medicos"),
    path('info/', info, name="info"),
    
    
   
    
    path('medico_form/', medicoForm, name="medico_form"),
    path('medico_form2/', medicoForm2, name="medico_form2"),
    path('paciente_form/', pacienteForm, name="paciente_form"),
    path('paciente_form2/', pacienteForm2, name="paciente_form2"),
    path('turno_form/', turnoForm, name="turno_form"),
    path('turno_form2/', turnoForm2, name="turno_form2"),

    
    
    path('buscar_medico/', buscarMedico, name="buscar_medico"),
    path('buscar2/', buscar2, name="buscar2"),


    path('pacientes/', pacientes, name="pacientes"),
    path('update_paciente/<id_paciente>/', updatePaciente, name="update_paciente"),
    path('delete_paciente/<id_paciente>/', deletePaciente, name="delete_paciente"),
    path('create_paciente/', createPaciente, name="create_paciente"),


    path('turnos/', TurnoList.as_view() , name="turnos"),
    path('create_turno/', TurnoCreate.as_view(), name="create_turno"),
    path('update_turno/<int:pk>/', TurnoUpdate.as_view(), name="update_turno"),
    path('delete_turno/<int:pk>/', TurnoDelete.as_view(), name="delete_turno"),
    

    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),

    path('registro/', register, name="registro"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('medicos/', MedicoList.as_view() , name="medicos"),
    path('create_medico/', MedicoCreate.as_view(), name="create_medico"),
    path('update_medico/<int:pk>/', MedicoUpdate.as_view(), name="update_medico"),
    path('delete_medico/<int:pk>/', MedicoDelete.as_view(), name="delete_medico"),


    path('empleados/', EmpleadoList.as_view() , name="empleados"),
    path('create_empleado/', EmpleadoCreate.as_view(), name="create_empleado"),
    path('update_empleado/<int:pk>/', EmpleadoUpdate.as_view(), name="update_empleado"),
    path('delete_empleado/<int:pk>/', EmpleadoDelete.as_view(), name="delete_empleado"),
]