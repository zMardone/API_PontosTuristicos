
from django.db.models.query import QuerySet
from rest_framework.serializers import ModelSerializer

from avaliacoes.models import Avaliacao
from rest_framework.serializers import ModelSerializer

class AvaliacoesSerializar(ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = ('id','user', 'comentario', 'nota', 'data')