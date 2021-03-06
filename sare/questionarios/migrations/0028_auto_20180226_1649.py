# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0027_auto_20180226_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='curso',
            field=models.CharField(choices=[('1', 'PROEJA - ATENDIMENTO'), ('2', 'PROEJA - MANUTENÇÃO E OPERAÇÃO DE MICROCOMPUTADORESs'), ('3', 'TEC. INT. - TÉCNICO EM ADMINISTRAÇÃO'), ('4', 'TEC. INT. - TÉCNICO EM AGRIMENSURA'), ('5', 'TEC. INT. - TÉCNICO EM AGRONEGÓCIO'), ('6', 'TEC. INT. - TÉCNICO EM CONTROLE AMBIENTAL '), ('7', 'TEC. INT. - TÉCNICO EM ELETROTÉCNICA'), ('8', 'TEC. INT. - TÉCNICO EM EVENTOS'), ('9', 'TEC. INT. - TÉCNICO EM INFORMÁTICA PARA INTERNET'), ('10', 'TEC. INT. - TÉCNICO EM MECATRÔNICA'), ('11', 'TEC. SUB. - TÉCNICO EM AGRIMENSURA'), ('12', 'TEC. SUB. - TÉCNICO EM AUTOMAÇÃO INDUSTRIAL'), ('30', 'TEC. SUB. - TÉCNICO EM CONTROLE AMBIENTAL'), ('13', 'TEC. SUB. - TÉCNICO EM EDIFICAÇÕES'), ('14', 'TEC. SUB. - TÉCNICO EM ELETROTÉCNICA'), ('15', 'TEC. SUB. - TÉCNICO EM INFORMÁTICA'), ('16', 'TEC. SUB. - TÉCNICO EM SECRETARIADO'), ('17', 'TEC. SUB. - TÉCNICO EM SEGURANÇA DO TRABALHO'), ('18', 'GRADUAÇÃO - ENGENHARIA CIVIL'), ('19', 'GRADUAÇÃO - ENGENHARIA ELÉTRICA'), ('20', 'GRADUAÇÃO - EDUCAÇÃO FÍSICA'), ('21', 'GRADUAÇÃO - FÍSICA'), ('22', 'GRADUAÇÃO - LETRAS - LÍNGUA PORTUGUESA'), ('23', 'GRADUAÇÃO - MATEMÁTICA'), ('24', 'GRADUAÇÃO - AGRONEGÓCIO'), ('25', 'GRADUAÇÃO - CONSTRUÇÃO DE EDIFÍCIOS'), ('26', 'GRADUAÇÃO - GESTÃO DE TURISMO'), ('27', 'GRADUAÇÃO - GESTÃO PÚBLICA'), ('28', 'GRADUAÇÃO - SISTEMAS ELÉTRICOS'), ('29', 'GRADUAÇÃO - SISTEMAS PARA INTERNET')], default=None, max_length=50, verbose_name='curso'),
        ),
    ]
