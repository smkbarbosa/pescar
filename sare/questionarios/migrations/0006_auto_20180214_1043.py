# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0005_auto_20180214_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionario',
            name='uuid',
        ),
        migrations.AddField(
            model_name='questionario',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
