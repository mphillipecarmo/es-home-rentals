from django.db import models
from django.db.models.fields import DateField, DateTimeField

BOOL_CHOICES = ((True, 'sim'), (False, 'nao'))

class Casa(models.Model):
    qtdeQuartos = models.IntegerField()
    qtdeSuites = models.IntegerField()
    qtdeSalaEstar = models.IntegerField()
    qtdeVagasGaragem = models.IntegerField()
    area = models.IntegerField()
    possuiArmarioEmbutido = models.BooleanField(choices=BOOL_CHOICES)
    descricao = models.TextField()
    aluguel = models.IntegerField(null=True,blank=True)
    endereco = models.TextField(null=True,blank=True)
    
class Apartamento(models.Model):
    qtdeQuartos = models.IntegerField()
    qtdeSuites = models.IntegerField()
    qtdeSalaEstar = models.IntegerField()
    qtdeSalaJantar = models.IntegerField()
    qtdeVagasGaragem = models.IntegerField()
    area = models.IntegerField()
    possuiArmarioEmbutido = models.BooleanField()
    descricao = models.TextField()
    andar = models.IntegerField()
    valorCondominio = models.FloatField()
    possuiPortaria = models.BooleanField()
    aluguel = models.IntegerField(null=True,blank=True)
    endereco = models.TextField(null=True,blank=True)

class HorarioMarcado(models.Model):
    nomeCliente = models.TextField(null=True,blank=True)
    data = models.DateTimeField(null=True,blank=True)
    id_imovel = models.IntegerField(null=True,blank=True)
    tipo_imovel = models.IntegerField(null=True, blank=True)