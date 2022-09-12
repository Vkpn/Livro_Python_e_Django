import json
from decimal import Decimal
from django.db import models
from django.urls import reverse


class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    data_ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('main:listar_produtos_por_categoria', args=[self.slug])


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    disponivel = models.BooleanField(default=True, verbose_name='Produto disponível?')
    estoque = models.PositiveIntegerField(verbose_name='Qtd. em estoque')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    data_ultima_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data da última atualização')
    imagem = models.ImageField(upload_to='imagens-produtos', blank=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    class DecimalEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal):
                return str(obj)
            return json.JSONEncoder.default(self, obj)

    def __str__(self):
        return str(self.nome)

    def get_absolute_url(self):
        return reverse('main:detalhes_produto', args=[self.slug])
