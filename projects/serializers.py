from rest_framework import serializers
from .models import Asignaturas, Alumnos, Agenda, Pago, Plataforma, Formapago, Profesor

class AsignaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignaturas
        fields = ('id', 'codigo', 'nombre', 'descripcion', 'fechacreacion')
        read_only_fields = ('fechacreacion', )
        

class AlumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('id', 'nombre', 'apellido', 'rut', 'correo', 'estado')

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ('id', 'fechaPago', 'idFormaPago', 'rutAlumno', 'valor', 'comision', 'estado', 'idAgenda')

class FormapagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formapago
        fields = ('id', 'nombre', 'fechaCreacion', 'estado')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id', 'fechaHorario', 'fechaHorarioFin', 'idAsignatura', 'datos_profe', 'idPlataforma', 'link', 'estado')

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ('id', 'nombre', 'fechacreacion', 'estado')

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id', 'rut', 'nombre', 'apellido', 'fechacreacion', 'estado')