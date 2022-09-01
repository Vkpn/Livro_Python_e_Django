from .carrinho import Carrinho


def carrinho(request):
    resultado = {
        'carrinho': Carrinho(request)
    }
    return resultado
