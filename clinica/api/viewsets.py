from rest_framework.viewsets import ModelViewSet
from clinica.models import Clinica
from .serializers import ClinicaSerializer


class ClinicaViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer
