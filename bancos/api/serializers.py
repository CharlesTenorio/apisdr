from rest_framework.serializers import ModelSerializer
from bancos.models import Banco


class BancoSerializer(ModelSerializer):
    class Meta:
        model = Banco
        fields = ['id', 'banco']
