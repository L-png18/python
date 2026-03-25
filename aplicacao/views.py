from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UsuarioForm, PerfilForm
from django.contrib.auth import login

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
    thisqtde = request.POST.get('txtQtde')
    thisdata = request.POST.get('txtData')
    thisdescricao = request.POST.get('txtDescricao')

    produto = Produto(
        nome = thisnome,
        preco = float(thispreco),
        qtde = thisqtde,
        data = thisdata,
        descricao = thisdescricao
    )

    produto.save()
    return redirect('urlproduto')

def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id)  
    #Produto.objects.get(id=id)

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