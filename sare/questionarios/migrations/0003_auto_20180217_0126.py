# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-17 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0002_auto_20180214_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='hashId',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
