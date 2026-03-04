from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    context = {'curso': 'Desenvolvimento de Sistemas'}
    return render(request, 'index.html', context)

def contato(request):
    context = {
        'nome': 'Instituto Federal de SC',
        'telefone': '(47) 3363-5251', 
        'email': 'contato@ifsc.edu.br'
    }
    return render(request, 'contato.html', context)

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
    #produto = Produto.objects.get(id=id)

    if request.method == 'GET':
        context = {'produto': produto}
        return render(request, "editarProduto.html", context)
    else: 
        thisnome = request.POST.get('txtNome')
        thispreco = request.POST.get('txtPreco').replace(',','.')
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
    produto = get_object_or_404(Produto,id=id)
    produto.delete()
    return redirect('urlproduto')

def entrar(request):

    if request.method == "GET":
        return render(request, "entrar.html")
    elif request.method == "POST":
        usuario = request.POST.get("txtUser")
        senha = request.POST.get("txtPass")
        return HttpResponse('entrou')

    