from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('criar/', views.criar_pedido, name='criar_pedido')
]