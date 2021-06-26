from endereco.models import Endereco
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacoesSerializar
from comentarios.api.serializers import ComentarioSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    avaliacoes = AvaliacoesSerializar(many=True)
    comentarios = ComentarioSerializer(many=True)


    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'foto', 'aprovado',
        'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
        'foto']

