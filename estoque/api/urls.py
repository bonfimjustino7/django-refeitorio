from rest_framework import routers
from estoque.api.viewset import *

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'tipo', TipoProdutoViewSet)
router.register(r'tipomovimentacao', TipoMovimentacaoViewSet)
router.register(r'movimentacao', MovimetacaoViewSet)
