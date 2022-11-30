from django.db import models

# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length=50)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    clave = models.CharField(max_length=10)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=60)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    rut = models.CharField(max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

    def nombre_rut(self):
        return "{} {}, {}".format(self.nombre, self.apellido , self.rut)

    def __str__(self):
        return self.nombre_rut()

class Asistencia(models.Model):
    rutAlumno = models.ForeignKey(Alumno, on_delete=models.PROTECT, null=True)
    estado = models.CharField(max_length=20)
    fechaAsistencia = models.DateTimeField(auto_now_add=True)

class Profesor(models.Model):
    rut = models.CharField(max_length=8)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    def nombre_rut(self):
        return "{} {}, {}".format(self.nombre, self.apellido , self.rut)

    def __str__(self):
        return self.nombre_rut()

class Plataforma(models.Model):
    nombre = models.CharField(max_length=60)
    fechacreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Agenda(models.Model):
    fechaHorario = models.DateTimeField(auto_now_add=True)
    fechaHorarioFin = models.DateTimeField(auto_now_add=True)
    idAsignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)
    rutProfesor = models.ForeignKey(Profesor, on_delete=models.PROTECT)
    idPlataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT)
    link = models.TextField(max_length=1000)
    estado = models.CharField(max_length=20)

class Forma(models.Model):
    nombre = models.CharField(max_length=20)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)

class Pago(models.Model):
    fechaPago = models.DateTimeField(auto_now_add=True)
    idFormaPago = models.ForeignKey(Forma, on_delete=models.PROTECT)
    rutAlumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    valor = models.IntegerField()
    comision = models.IntegerField()
    estado = models.CharField(max_length=20)
    idAgenda = models.ForeignKey(Agenda, on_delete=models.PROTECT)
