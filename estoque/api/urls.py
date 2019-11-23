from rest_framework import routers
from estoque.api.viewset import ProdutoViewSet


router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
