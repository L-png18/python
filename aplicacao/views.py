from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto, Venda, ItemVenda, Perfil 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UsuarioForm, PerfilForm
from django.contrib.auth import login


### CARRINHO ####
def get_or_create_carrinho(request):
    venda, created = Venda.objects.get_or_create(
        cliente = request.user,
        status = 'P' # Venda Pendente
    )
    return venda

def vercarrinho(request):
    venda = get_or_create_carrinho(request)
    itens = venda.itemvenda_set.all()
    perfil = getattr(request.user, 'perfil', None)

    context = {
        'venda': venda,
        'itens': itens,
        'perfil': perfil
    }

    return render(request, 'vercarrinho.html', context)

def atualizarcarrinho(request, item_id):
    item = get_object_or_404(ItemVenda, id=item_id, venda__cliente=request.user)

    if request.method == 'POST':
        acao = request.POST.get('acao')
        if item.qtde < item.produto.qtde:
            item.qtde += 1
            item.save()
        elif acao == 'diminuir':
            if item.qtde > 1:
                item.qtde -= 1
                item.save()
            else: # se for 1 e diminuir, então remove
                item.delete()
        elif acao == 'remover':
            item.delete()
    return redirect('vercarrinho')

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'index.html', {'produtos': produtos})


def contato(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'contato.html', context)


@login_required(login_url="urlentrar")
def produto(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "produto.html", context)


def cadastrarProduto(request):
    return render(request, "cadastrarProduto.html")


def salvarProduto(request):
    thisnome = request.POST.get('txtNome')
    thispreco = request.POST.get('txtPreco')
    thisqtde = int(request.POST.get('txtQtde'))
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')
    thisimagem = request.FILES.get('txtImagem')

    produto = Produto(
        nome=thisnome,
        preco=float(thispreco),
        qtde=thisqtde,
        data=thisdata,
        descricao=thisdescricao,
        imagem=thisimagem
    )

    produto.save()
    return redirect('urlproduto')


def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == "GET":
        context = {'p': produto}
        return render(request, "editarProduto.html", context)
    else:
        thisnome = request.POST.get('txtNome')
        thispreco = request.POST.get('txtPreco').replace(',', '.')
        thisqtde = request.POST.get('txtQtde')
        thisdata = request.POST.get('txtData')
        thisdescricao = request.POST.get('txtDescricao')

        produto.nome = thisnome
        produto.preco = float(thispreco)
        produto.qtde = thisqtde
        produto.data = thisdata
        produto.descricao = thisdescricao

        produto.save()
        return redirect('urlproduto')


def excluirProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('urlproduto')


def entrar(request):
    if request.method == "GET":
        return render(request, "entrar.html")
    elif request.method == "POST":
        usuario = request.POST.get("txtUser")
        senha = request.POST.get("txtPass")
        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return redirect('urlproduto')
        messages.error(request, "Falha na autenticação!")
        return render(request, 'entrar.html')


def sair(request):
    logout(request)
    return redirect('urlentrar')


def cadastrarUsuario(request):
    if request.method == "POST":
        user_form = UsuarioForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save(commit=False)
            user.save()

            perfil = perfil_form.save(commit=False)
            perfil.cliente = user
            perfil.save()

            login(request, user)
            return redirect('urlindex')
    else:
        user_form = UsuarioForm()
        perfil_form = PerfilForm()

    return render(request, 'cadastrarUsuario.html', {'user_form': user_form, 'perfil_form': perfil_form})


@login_required(login_url="urlentrar")
def criarVenda(request):
    venda = Venda.objects.create(cliente=request.user)
    return redirect('urlAdicionarItem', venda_id=venda.id)


@login_required(login_url="urlentrar")
def adicionarItem(request, venda_id):
    venda = get_object_or_404(Venda, id=venda_id)

    if request.method == "POST":
        produto_id = request.POST.get('produto_id')
        qtde = request.POST.get('qtde')

        if not qtde:
            messages.error(request, "Informe a quantidade")
            return redirect('urlAdicionarItem', venda_id=venda.id)

        quantidade = int(qtde)

        produto = get_object_or_404(Produto, id=produto_id)

        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            qtde=quantidade
        )

    produtos = Produto.objects.all()
    itens = ItemVenda.objects.filter(venda=venda)

    return render(request, 'adicionarItem.html', {
        'venda': venda,
        'produtos': produtos,
        'itens': itens
    })


@login_required(login_url="urlentrar")
def listarVendas(request):
    vendas = Venda.objects.filter(cliente=request.user)
    return render(request, 'listarVendas.html', {'vendas': vendas})