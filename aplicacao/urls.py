from django.urls import path
from .views import (
    index, contato, produto, entrar, sair,
    cadastrarProduto, salvarProduto, editarProduto, excluirProduto,
    cadastrarUsuario,
)
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('', index, name="urlindex"),
    path('contato/', contato, name="urlcontato"),
    path('produto/', produto, name="urlproduto"),
    path('cadastrarProduto/', cadastrarProduto, name="urlcadastrarProduto"),
    path('salvarProduto/', salvarProduto, name="urlsalvarProduto"),
    path('editarProduto/<int:id>/', editarProduto, name="urleditarProduto"),
    path('excluirProduto/<int:id>/', excluirProduto, name="urlexcluirProduto"),
    path('entrar/', entrar, name="urlentrar"),
    path('sair/', sair, name="urlsair"),
    path('cadastrarUsuario/', cadastrarUsuario, name="urlcadastrarUsuario"),
    path('pedido/<int:venda_id>', views.detalhe_pedido, name='urldetalhe_pedido'),
    path('historico/', views.historico_pedidos, name='urlhistorico'),

    ### Carrinho
    path('vercarrinho', views.vercarrinho, name="urlvercarrinho"),
    path('vercarrinho/atualizar/<int:item_id>/', views.atualizarcarrinho, name="urlatualizarcarrinho"),
    path('vercarrinho/adicionar/<int:produto_id>/', views.adicionarcarrinho, name="urladicionarcarrinho"),
    path('vercarrinho/finalizar/', views.finalizarcompra, name="urlfinalizarcompra"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)