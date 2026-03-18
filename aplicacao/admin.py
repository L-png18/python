from django.contrib import admin

from .models import Produto, Perfil, Venda, ItemVenda

@admin.register(Produto)
class ProdutoAdm(admin).ModelAdmin:
    list_display = ('id', 'nome', 'preco', 'qtde', 'data')
    list_display_link = ('nome', )
    search_fields = ('nome',)
    list_filter = ('preco', 'qtde')

@admin.register(Perfil)
class Perfil


