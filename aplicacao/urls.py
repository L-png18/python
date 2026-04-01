from django.urls import path
from .views import (
    index, contato, produto, entrar, sair,
    cadastrarProduto, salvarProduto, editarProduto, excluirProduto,
    cadastrarUsuario,
    criarVenda, adicionarItem, listarVendas  
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
    path('venda/criar/', criarVenda, name='urlCriarVenda'),
    path('venda/<int:venda_id>/item/', adicionarItem, name='urlAdicionarItem'),
    path('vendas/', listarVendas, name='urlListarVendas'),

    ### Carrinho
    path('vercarrinho', views.vercarrinho, name="urlvercarrinho"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)