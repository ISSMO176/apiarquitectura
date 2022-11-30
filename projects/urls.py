from rest_framework import routers
from .api import AsignaturaViewSet, AlumnosViewSet, PagoViewSet, FormapagoViewSet , AgendaViewSet , PlataformaViewSet , ProfesorViewSet, AsistenciaViewSet

router = routers.DefaultRouter()

router.register('api/admin', AsignaturaViewSet, 'asignaturas')
router.register('api/asignaturas', AsignaturaViewSet, 'asignaturas')
router.register('api/alumnos', AlumnosViewSet, 'alumnos')
router.register('api/pago', PagoViewSet, 'pago')
router.register('api/formapago', FormapagoViewSet, 'formapago')
router.register('api/agenda', AgendaViewSet, 'agenda')
router.register('api/plataforma', PlataformaViewSet, 'plataforma')
router.register('api/profesor', ProfesorViewSet, 'profesor')
router.register('api/asistencia', AsistenciaViewSet, 'asistencia')



urlpatterns = router.urls