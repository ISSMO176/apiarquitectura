from rest_framework import serializers
from .models import Administrador,Asignatura, Alumno, Asistencia, Agenda, Pago, Plataforma, Forma, Profesor


class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ('id', 'nombre', 'fechacreacion', 'clave')
        read_only_fields = ('fechacreacion', )

class AsignaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id', 'nombre', 'fechacreacion', 'estado')
        read_only_fields = ('fechacreacion', )
        
class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id', 'rut', 'nombre', 'apellido', 'fechacreacion', 'estado')

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('id', 'rutAlumno', 'estado', 'fechaAsistencia')

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id', 'fechaPago', 'idFormaPago', 'Datos Alumno', 'valor', 'comision', 'estado', 'idAgenda')

class FormapagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forma
        fields = ('id', 'nombre', 'fechaCreacion', 'estado')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'fechaHorario', 'fechaHorarioFin', 'idAsignatura', 'rutProfesor', 'idPlataforma', 'link', 'estado')

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ('id', 'nombre', 'fechacreacion', 'estado')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'rut', 'nombre', 'apellido', 'fechacreacion', 'estado')