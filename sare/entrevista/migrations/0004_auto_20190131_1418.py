# Generated by Django 2.1.5 on 2019-01-31 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrevista', '0003_auto_20180524_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrevista',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionarios.QuestionarioOld'),
        ),
    ]
