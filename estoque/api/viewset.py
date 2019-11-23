from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from estoque.models import Produto
from estoque.api.serializers import *

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers

class TipoProdutoViewSet(ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoProdutoSerializers

class TipoMovimentacaoViewSet(ModelViewSet):
    queryset = TipoMovimentacao.objects.all()
    serializer_class = TipoMovimentacaoSerializers

class MovimetacaoViewSet(ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializers

    #Impedindo de movimentação ser atualizada ou excluida
    def update(self, request, *args, **kwargs):
        return Response({'msg': 'Movimentação não pode ser atualizada ou excluida, faça uma nova movimentação como estorno.'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        return Response({'msg': 'Movimentação não pode ser atualizada ou excluida, faça uma nova movimentação como estorno.'}, status=status.HTTP_401_UNAUTHORIZED)