from django.db import models

# Create your models here.

class Asignaturas(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    fechacreacion = models.DateTimeField(auto_created=True)

class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    rut = models.CharField(max_length=9)
    correo = models.CharField(max_length=200)
    estado = models.CharField(max_length=150)

class Pago(models.Model):
    fechaPago = models.DateTimeField(auto_now_add=True)
    idFormaPago = models.ForeignKey(Formapago, on_delete=models.PROTECT)
    rutAlumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    valor = models.IntegerField()
    comision = models.IntegerField()
    estado = models.CharField(max_length=20)
    idAgenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)

class Formapago(models.Model):
    nombre = models.CharField(max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Agenda(models.Model):
    fechaHorario = models.DateTimeField(auto_now_add=True)
    fechaHorarioFin = models.DateTimeField(auto_now_add=True)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    datos_profe = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    idPlataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    link = models.TextField(max_length=100)
    estado = models.CharField(max_length=20)

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)


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