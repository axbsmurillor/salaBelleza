# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20170613_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='idcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
