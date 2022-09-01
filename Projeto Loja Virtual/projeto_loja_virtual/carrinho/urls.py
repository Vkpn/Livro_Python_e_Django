from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('', views.detalhes_carrinho, name='detalhes_carrinho'),
    path('adicionar/<int:id_produto>', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:id_produto>', views.remover_do_carrinho, name='remover_do_carrinho'),
]
