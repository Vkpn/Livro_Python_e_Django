from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Produto
from .carrinho import Carrinho
from .forms import FormAdicionarProdutoAoCarrinho


@require_POST
def adicionar_ao_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    form = FormAdicionarProdutoAoCarrinho(request.POST)
    if form.is_valid():
        dados = form.cleaned_data
        carrinho.adicionar(produto=produto, quantidade=dados['quantidade'], atualizar_quantidade=dados['atualizar'])
    return redirect('carrinho:detalhes_carrinho')


def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('carrinho:detalhes_carrinho')


def detalhes_carrinho(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['formulario_adicionar_produto_ao_carrinho'] = FormAdicionarProdutoAoCarrinho(initial={'quantidade': item['quantidade'], 'atualizar': True})
    return render(request, 'carrinho/detalhes.html', {'carrinho': carrinho})
