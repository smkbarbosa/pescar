# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0032_auto_20180405_1509'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='dimensao_ambiental',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoAmbiental'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='dimensao_cultural',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoCultural'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='dimensao_economica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoEconomica'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='dimensao_social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoSocial'),
        ),
    ]
