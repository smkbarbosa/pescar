# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-16 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrevista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevista',
            name='fn_7',
            field=models.TextField(max_length=800, null=True, verbose_name='Justifique'),
        ),
        migrations.AlterField(
            model_name='entrevista',
            name='per_dependentes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Dependentes da Renda'),
        ),
    ]
