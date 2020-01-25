from django.contrib import admin
from django.urls import path
from rest_framework import routers
from clinica.api.viewsets import ClinicaViewSet
from django.conf.urls import include


router = routers.SimpleRouter()
router.register(r'api/clinica', ClinicaViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
