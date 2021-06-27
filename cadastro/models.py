from django.db import models

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