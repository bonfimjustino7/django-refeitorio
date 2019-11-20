from django.db import models

class Tipo(models.Model):
    tipo = models.CharField(max_length=20)

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)

class TipoMovimentacao(models.Model):
    nome_movimentacao = models.CharField(max_length=50)
    fator = models.IntegerField()

class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    tipo_movimentacao = models.ForeignKey(TipoMovimentacao, on_delete=models.DO_NOTHING)
    data = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField()