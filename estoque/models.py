from django.db import models
from django.utils.html import mark_safe

class Tipo(models.Model):
    tipo = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.tipo

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome_produto

class TipoMovimentacao(models.Model):
    nome_movimentacao = models.CharField(max_length=50)
    fator = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Tipo de Movimentações'

    def __str__(self):
        return self.nome_movimentacao

class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    tipo_movimentacao = models.ForeignKey(TipoMovimentacao, on_delete=models.DO_NOTHING)
    data = models.DateField(auto_now_add=True)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Movimentações'

    def __str__(self):
        return str(self.produto) + ' - ' + str(self.tipo_movimentacao) + ' - ' + str(self.quantidade) + ' - ' + str(self.data)