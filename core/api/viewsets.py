from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PontoTuristicoSerializer
    # olhar possibilidades no searchfilter
    filter_backends = (SearchFilter,)
    filter_fields = ('nome', 'descricao', 'endereco__linha1')

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome=nome)
        
        if descricao:
            queryset = queryset.filter(descricao=descricao)

        return queryset
    
    # Criando GET
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Criando Create
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Precisa ser passado o ID, bem legal para sobrescrever para
    # pegar quem deletou ou outro tipo de informação
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    # funciona pelo metodo get também, mas fazer validações extras
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs) 
    
    # Necessario passar id para saber a qual id se refere
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # PATCH, muda apenas um campo, update faz o mesmo mas não é boa pratica
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    # criando novas rotas
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({'teste': 123})
