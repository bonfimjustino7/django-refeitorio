from rest_framework.response import Response
from rest_framework.serializers import *
from estoque.models import *

class TipoProdutoSerializers(ModelSerializer):

    class Meta:
        model = Tipo
        fields = ['id', 'tipo']

class ProdutoSerializers(ModelSerializer):
    tipo = TipoProdutoSerializers(read_only=True)
    tipo_id = PrimaryKeyRelatedField(write_only=True, queryset=Tipo.objects.all())

    class Meta:
        model = Produto
        fields = ['id', 'nome_produto', 'tipo', 'tipo_id']

    def create(self, validated_data):
        tipo = validated_data.pop('tipo_id')
        produto = Produto.objects.create(**validated_data, tipo_id=tipo.id)

        return produto

    def update(self, instance, validated_data):
        tipo = validated_data.pop('tipo_id')
        instance.nome_produto = validated_data.get('nome_produto')
        instance.tipo_id = tipo.id
        instance.save()

        return instance

class TipoMovimentacaoSerializers(ModelSerializer):

    class Meta:
        model = TipoMovimentacao
        fields = ['nome_movimentacao', 'fator']

class MovimentacaoSerializers(ModelSerializer):
    produto = ProdutoSerializers(read_only=True)
    produto_id = PrimaryKeyRelatedField(write_only=True, queryset=Produto.objects.all())
    tipo_movimentacao = TipoMovimentacaoSerializers(read_only=True)
    tipo_movimentacao_id = PrimaryKeyRelatedField(write_only=True, queryset=TipoMovimentacao.objects.all())

    class Meta:
        model = Movimentacao
        fields = ['id', 'produto', 'produto_id', 'tipo_movimentacao', 'tipo_movimentacao_id', 'data', 'quantidade']

    def create(self, validated_data):
        produto_id = validated_data.pop('produto_id')
        tipo_movimentacao_id = validated_data.pop('tipo_movimentacao_id')

        movimentacao = Movimentacao.objects.create(produto_id = produto_id.id, tipo_movimentacao_id=tipo_movimentacao_id.id, **validated_data)

        return movimentacao

    #def update(self, instance, validated_data):
        # produto = validated_data.pop('produto_id')
        # tipo_movimentacao = validated_data.pop('tipo_movimentacao_id')
        # quantidade = validated_data.get('quantidade')
        # instance.produto = produto
        # instance.tipo_movimentacao = tipo_movimentacao
        # instance.quantidade = quantidade
        # instance.save()
        #return instance
