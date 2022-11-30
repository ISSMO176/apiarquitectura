from .models import Asignaturas
from rest_framework import viewsets, permissions
from .serializers import AsignaturasSerializer, AlumnosSerializer, PagoSerializer, FormapagoSerializer, AgendaSerializer, PlataformaSerializer, ProfesorSerializer

class AsignaturasViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AsignaturasSerializer

class AlumnosViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlumnosSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer

class FormapagoViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FormapagoSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgendaSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlataformaSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Asignaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProfesorSerializer