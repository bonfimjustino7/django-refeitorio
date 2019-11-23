from rest_framework.viewsets import ModelViewSet
from estoque.models import Produto
from estoque.api.serializers import *

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers