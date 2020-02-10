from rest_framework.viewsets import ModelViewSet
from bancos.models import Banco
from .serializers import BancoSerializer


class BancoViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer
