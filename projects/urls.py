from rest_framework import routers
from .api import AsignaturasViewSet, AlumnosViewSet, PagoViewSet, FormapagoViewSet , AgendaViewSet , PlataformaViewSet , ProfesorViewSet

router = routers.DefaultRouter()

router.register('api/asignaturas', AsignaturasViewSet, 'asignaturas')
router.register('api/alumnos', AlumnosViewSet, 'alumnos')
router.register('api/pago', PagoViewSet, 'pago')
router.register('api/formapago', FormapagoViewSet, 'formapago')
router.register('api/agenda', AgendaViewSet, 'agenda')
router.register('api/plataforma', PlataformaViewSet, 'plataforma')
router.register('api/profesor', ProfesorViewSet, 'profesor')



urlpatterns = router.urls