from django.db import models
from decimal import Decimal
from main.models import Produto


class Pedido(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    data_criacao = models.DateField(auto_now=True)
    pago = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_criacao',)

    def __str__(self):
        return 'Pedido #' + str(self.id)

    def get_total_geral(self):
        resultado = Decimal(0.0)
        for item in self.itens.all():
            subtotal = Decimal(item['quantidade']) * Decimal(item['preco'])
            resultado = resultado + subtotal
        return float(resultado)


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Pedido #' + str(self.id)

    def get_subtotal(self):
        subtotal = self.preco * self.quantidade
        return float(subtotal)

