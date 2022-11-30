from .models import Asistencia, Asignatura, Pago, Alumno, Profesor, Plataforma, Forma, Agenda
from rest_framework import viewsets, permissions
from .serializers import AsignaturasSerializer, AlumnosSerializer, PagoSerializer, FormapagoSerializer, AgendaSerializer, PlataformaSerializer, ProfesorSerializer, AsistenciaSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturasSerializer

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsistenciaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PagoSerializer

class FormapagoViewSet(viewsets.ModelViewSet):
    queryset = Forma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormapagoSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgendaSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlataformaSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer