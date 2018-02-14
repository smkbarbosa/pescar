# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0002_auto_20180214_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
