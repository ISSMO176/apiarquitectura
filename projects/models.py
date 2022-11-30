from django.db import models

from projects.api import ProfesorViewSet

# Create your models here.

class Asignaturas(models.Model):
    nombre = models.CharField(max_length=60)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre


class Alumnos(models.Model):
    rut = models.CharField(max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

    def nombre_rut(self):
        return "{} {}, {}".format(self.nombre, self.apellido , self.rut)

    def __str__(self):
        return self.nombre_rut()

class Formapago(models.Model):
    nombre = models.CharField(max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Agenda(models.Model):
    fechaHorario = models.DateTimeField(auto_now_add=True)
    fechaHorarioFin = models.DateTimeField(auto_now_add=True)
    idAsignatura = models.ForeignKey(Asignaturas, on_delete=models.PROTECT)
    datos_profe = models.ForeignKey(ProfesorViewSet, on_delete=models.PROTECT)
    idPlataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    link = models.TextField(max_length=100)
    estado = models.CharField(max_length=20)

class Pago(models.Model):
    fechaPago = models.DateTimeField(auto_now_add=True)
    idFormaPago = models.ForeignKey(Formapago, on_delete=models.PROTECT)
    rutAlumno = models.ForeignKey(Alumnos, on_delete=models.PROTECT)
    valor = models.IntegerField()
    comision = models.IntegerField()
    estado = models.CharField(max_length=20)
    idAgenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)

class Profesor(models.Model):
    rut = models.CharField(max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    def datos_profe(self):
        return "{} {}, {}".format(self.nombre, self.apellido , self.rut)

    def __str__(self):
        return self.datos_profe()

class Asistencia(models.Model):
    rutAlumno = models.ForeignKey(Alumnos, on_delete=models.PROTECT, null=True)
    estado = models.CharField(max_length=20)
    fechaAsistencia = models.DateTimeField(auto_now_add=True)
