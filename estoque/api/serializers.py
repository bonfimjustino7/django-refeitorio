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
    # TODO implementar rota que atualiza o produto
    # def update(self, instance, validated_data):
    #
    #
    #     return instance