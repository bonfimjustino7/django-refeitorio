from django.contrib import admin
from django.contrib.admin import register
from estoque.models import *

@register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'tipo')

@register(TipoMovimentacao)
class TipoMovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('nome_movimentacao', 'fator')

@register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'data', 'quantidade')
 #   change_list_template = 'admin/estoque/movimentacao/change_list.html'

    def get_saldo(self, request):
        saldo = 0
        if request.GET.get('q', False):
            movs = Movimentacao.objects.filter(produto__nome_produto=request.GET['q'])
        else:
            movs = Movimentacao.objects.all()
        for m in movs:
            saldo += m.quantidade
        return saldo

    def changelist_view(self, request, extra_context=None):
        context = {
            'total': self.get_saldo(request)
        }
        return super(MovimentacaoAdmin, self).changelist_view(request, extra_context=context)

    def get_queryset(self, request):
        if not request.GET.get('q', False):
            return super(MovimentacaoAdmin, self).get_queryset(request)
        return Movimentacao.objects.filter(produto__nome_produto=request.GET['q'])