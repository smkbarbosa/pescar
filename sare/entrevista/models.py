# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


#Dados dos alunos
from sare.core.models import Aluno

#Reversion auditoria nos logs
import reversion

# Create your models here.

@reversion.register
class Entrevista(models.Model):
    aluno = models.ForeignKey(Aluno)

    # Classificacao renda percapita (PER)

    per_renda_bruta = models.DecimalField('Renda Bruta Familiar', max_digits=8, decimal_places=2, default=0.0)
    per_dependentes = models.DecimalField('Dependentes da Renda', max_digits=8, decimal_places=2, default=0.0)
    # Variaveis dedutives
    per_imposto_renda = models.DecimalField('Imposto de Renda', max_digits=8, decimal_places=2, default=0.0)
    per_previdencia = models.DecimalField('Previdência', max_digits=8, decimal_places=2, default=0.0)


    # Despesas (D)

    d_tratamento_saude = models.DecimalField('Tratamento de Saúde', max_digits=8, decimal_places=2, default=0.0)
    d_medicamentos = models.DecimalField('Medicamentos', max_digits=8, decimal_places=2, default=0.0)
    d_cuidador = models.DecimalField('Cuidador/Idoso/PNE', max_digits=8, decimal_places=2, default=0.0)
    d_plano_saude = models.DecimalField('Plano de Saúde', max_digits=8, decimal_places=2, default=0.0)
    d_educacao_superior = models.DecimalField('Educação Superior', max_digits=8, decimal_places=2, default=0.0)
    d_ensino_basico = models.DecimalField('Ensino Básico', max_digits=8, decimal_places=2, default=0.0)
    d_cursos_prep = models.DecimalField('Cursos Preparatórios', max_digits=8, decimal_places=2, default=0.0)
    d_capacitacao = models.DecimalField('Capacitação', max_digits=8, decimal_places=2, default=0.0)
    d_transporte = models.DecimalField('Transporte', max_digits=8, decimal_places=2, default=0.0)
    d_aluguel = models.DecimalField('Aluguel/Financiamento', max_digits=8, decimal_places=2, default=0.0)
    d_financiamento_carro = models.DecimalField('Financiamento de carro', max_digits=8, decimal_places=2, default=0.0)
    d_financiamento_moto = models.DecimalField('Financiamento de moto', max_digits=8, decimal_places=2, default=0.0)
    d_terreno = models.DecimalField('Terreno/Lote', max_digits=8, decimal_places=2, default=0.0)
    d_energia = models.DecimalField('Energia', max_digits=8, decimal_places=2, default=0.0)
    d_agua = models.DecimalField('Água', max_digits=8, decimal_places=2, default=0.0)
    d_alimentacao = models.DecimalField('Alimentação', max_digits=8, decimal_places=2, default=0.0)

    # Checklist de Documentos (CL)

    cl_1 = models.BooleanField('Cópia Legível do RG e CPF do candidato', default=False)
    cl_2 = models.BooleanField('Cópia Legível do RG e CPF do responsável legal (caso o candidato seja menor de idade)', default=False)
    cl_3 = models.BooleanField('Comprovante de renda recente de todos os integrantes do grupo familiar que trabalham (que residem juntos)', default=False)
    cl_4 = models.BooleanField('Não tendo comprovante de renda, apresentar declaração de ausência de renda, conforme o modelo ANEXO I', default=False)
    cl_5 = models.BooleanField('Comprovante de desemprego (se for o caso apresentar carteira de trabalho - folha de rosto e as páginas com registros -, aviso prévio ou outro documento que comprove a situação \
    de desmprego) ou decalração de ausência de renda conforme modelo ANEXO II', default=False)
    cl_6 = models.BooleanField('Comprovante de pagamento de aluguel (se for o caso) de  pagamento de prestação da casa própira (se imóvel financiado)', default=False)
    cl_7 = models.BooleanField('Comprovante recente de despesa com conta de água', default=False)
    cl_8 = models.BooleanField('Comprovante recente de despesa com conta de energia', default=False)
    cl_9 = models.BooleanField('Comprovante recente de pensão alimentícia (paga ou recebida pelo estudante), caso se enquadre em seu contexto sociofamiliar, conforme \
    modelo ANEXO III ou ANEXO IV', default=False)
    cl_10 = models.BooleanField('Comprovante do Número de Inscrição Social - NIS, (Folha Resumo do Cadúnico), caso se enquadre em seu contexto sociofamiliar', default=False)
    cl_11 = models.BooleanField('Aos candidatos que concorrem no perfil II, na modalidade creche, deverão apresentar a cópia de certidão de nascimento dos filhos', default=False)

    # Situações Problemas (SP)

    sp_1 = models.PositiveIntegerField('Dependente financeiro e sofre algum tipo de violência do responsável pelo seu sustento',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_2 = models.PositiveIntegerField('Veio de outra localidade com objetivo de estudar no IFTO',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_3 = models.PositiveIntegerField('Utiliza transporte intermunicipal o u rural para acessar o Campus',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_4 = models.PositiveIntegerField('Ser estudante em tempo integral',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_5 = models.PositiveIntegerField('Residir distante do Campus',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_6 = models.PositiveIntegerField('Necessita fazer refeições diárias no Campus',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_7 = models.PositiveIntegerField('Possui filhos entre 0 e 12 anos que estudam em instituições privadas',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_8 = models.PositiveIntegerField('Necessidade de pagar cuidador (idoso/criança) por não possuir nenhum responsável durante o período que está estudando no Campus',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_9 = models.PositiveIntegerField('Morar com o(s) filho(s) no mesmo ambiente familiar',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_10 = models.PositiveIntegerField('Desenvolver ou praticar qualquer modadilidade esportiva no Campus com acompanhamento do Professor',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_11 = models.PositiveIntegerField('Frequentar curso que esija material de uso pessoal e que seja específico do curso',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_12 = models.PositiveIntegerField('Ter carga horária disponível que não afete o desenvolvimento escolar',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_13 = models.PositiveIntegerField('Estudante vai ao Campus mais de 3 dias na semana para cursar disciplinas',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_14 = models.PositiveIntegerField('Aluno sai do trabalho e vai direto para o Campus',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sp_15 = models.PositiveIntegerField('Situação de doença crônica ou grave impacto na renda familiar',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    sp_16 = models.PositiveIntegerField('Não tem com quem deixar o(s) filho(s) para estudar',default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    # Finalização da Entrevista (FN)

    fn_1 = models.PositiveIntegerField('Condição de renda oriunda da informalidade', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_2 = models.PositiveIntegerField('Adulto ou chefe de família com baixa escolaridade', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_3 = models.PositiveIntegerField('Dependência de renda de idoso', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_4 = models.PositiveIntegerField('Domicílio em precário estado de construção apresentando sinais de fragilidades na estrutura', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_5 = models.PositiveIntegerField('Aluno com problemas graves indentificadas durante a entrevista', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_6 = models.PositiveIntegerField('Condição de renda oriunda da informalidade', default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fn_7 = models.TextField('Justifique', max_length=800, null=True)


    def __unicode__(self):
        return self.aluno.nome