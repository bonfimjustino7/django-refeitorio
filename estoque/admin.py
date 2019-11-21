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
    list_display = ('produto', 'tipo_movimentacao', 'data', 'quantidade')
    change_list_template = 'admin/estoque/change_list.html'
    list_filter = ('produto__nome_produto', )

    def get_saldo(self):
        movs = Movimentacao.objects.all()
        saldo = 0
        for m in movs:
            saldo += m.quantidade * m.tipo_movimentacao.fator
        return saldo

    def changelist_view(self, request, extra_context=None):
        context = {
            'total': self.get_saldo()
        }
        return super(MovimentacaoAdmin, self).changelist_view(request, extra_context=context)