from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from endereco.models import Endereco

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)

    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    enderecos = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True, blank=True)

    # foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)

    # exemplo de campo customizado, é possivel chamar ele no serializer fields
    @property
    def campo_customizado(self):
        return (self.nome + '' + self.descricao)

    def __str__(self):
        return self.nome