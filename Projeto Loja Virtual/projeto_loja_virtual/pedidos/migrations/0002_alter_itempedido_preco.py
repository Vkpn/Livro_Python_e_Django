# Generated by Django 4.1 on 2022-09-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempedido',
            name='preco',
            field=models.CharField(max_length=6),
        ),
    ]
