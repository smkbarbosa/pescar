# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionario',
            options={'ordering': ('-criado_em',), 'verbose_name': 'questionário', 'verbose_name_plural': 'questionários'},
        ),
        migrations.AlterField(
            model_name='questionario',
            name='bairro',
            field=models.CharField(max_length=100, null=True, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='cidade',
            field=models.CharField(max_length=100, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='fale_mais_familia',
            field=models.CharField(max_length=500, null=True, verbose_name='Fale mais sobre sua família'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True, verbose_name='sexo'),
        ),
    ]
