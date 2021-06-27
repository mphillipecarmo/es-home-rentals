from django import forms
from .models import *

class FormCasa(forms.Form):
    qtdeQuartos = forms.IntegerField()
    qtdeSuites = forms.IntegerField()
    qtdeSalaEstar = forms.IntegerField()
    qtdeVagasGaragem = forms.IntegerField()
    area = forms.IntegerField()
    possuiArmarioEmbutido = forms.BooleanField()
    descricao = forms.CharField()
    rua = forms.CharField()
    numero = forms.CharField()
    bairro = forms.CharField()
    cidade = forms.CharField()
    aluguel = forms.IntegerField()

class FormApartamento(forms.Form):
    qtdeQuartos = forms.IntegerField()
    qtdeSuites = forms.IntegerField()
    qtdeSalaEstar = forms.IntegerField()
    qtdeVagasGaragem = forms.IntegerField()
    qtdeSalaJantar = forms.IntegerField()
    area = forms.IntegerField()
    possuiArmarioEmbutido = forms.BooleanField()
    descricao = forms.CharField()
    andar = forms.IntegerField()
    valorCondominio = forms.FloatField()
    possuiPortaria = forms.BooleanField()
    rua = forms.CharField()
    numero = forms.CharField()
    bairro = forms.CharField()
    cidade = forms.CharField()
    aluguel = forms.IntegerField()