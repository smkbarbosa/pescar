# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180405_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='dimensao_ambiental',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='dimensao_cultural',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='dimensao_economica',
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='dimensao_social',
        ),
    ]
