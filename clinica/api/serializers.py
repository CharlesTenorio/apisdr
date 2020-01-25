from rest_framework.serializers import ModelSerializer
from clinica.models import Clinica


class ClinicaSerializer(ModelSerializer):
    class Meta:
        model = Clinica
        fields = ['id', 'nome', 'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'localidade', 'uf', 'fone',
                  'fone', 'fone1', 'pontuacao', 'token', 'cnpj', 'ativo', 'imagem', 'email', 'senha', 'token_fcm',
                  'data_cad']

        read_only_fields = ['id_usuario']
