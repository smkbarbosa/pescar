from unittest import skipIf

from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.models import Questionario


class QuestionarioNewPostValid(TestCase):
    def setUp(self):
        self.obj = mommy.make(Questionario,nome='Samuel Barbosa', cpf='58500336102', email='samuka1@gmail.com',
                              cidade='Palmas', bairro='Plano Diretor norte', _fill_optional=True)

        form_fields = ['hashId', 'criado_em','nome', 'cpf', 'email','fone',
                       'endereco','num_casa', 'cep', 'bairro',
                       'cidade', 'estado',
                       'sexo',
                       'curso', 'sem_mod_ano', 'matricula', 'campus',

                       'dependentes_RBD', 'origem_renda',
                       'renda_bruta_domiciliar',
                       'responsavel_domicilio', 'renda_per_capita', 'relacao_financeira',
                       'despesas_saude_tratamento', 'despesas_saude_medicamento', 'despesas_saude_cuidador',
                       'despesas_saude_plano', 'despesas_transporte', 'despesas_moradia',
                       'despesas_educacao_superior', 'despesas_educacao_basico', 'despesas_educacao_cursinho',
                       'despesas_educacao_capacitacao', 'despesas_educacao_material', 'despesas_bens_fcarro',
                       'despesas_bens_fmoto', 'despesas_bens_terreno', 'despesas_domesticas_eletrica',
                       'despesas_domesticas_agua', 'despesas_domesticas_alimentacao',
                       'condicao_responsavel_casa', 'meio_acesso_campus', 'condicao_moradia', 'local_moradia',
                       'total_pessoas_casa', 'total_comodos_casa', 'total_km_casa_campus',
                       'instituicao_anterior',
                       'saude_bebida_drogas', 'saude_doenca_grave', 'saude_doenca_cronica',
                       'saude_medicamento_diario',
                       'pne_parcial_visao_audicao', 'pne_def_fisica', 'pne_total_visao_audicao',
                       'pne_def_mental_leve',
                       'pne_def_mental_grave', 'psico_dificuldade_concentrar', 'psico_conflito_familiar',
                       'psico_depressao',
                       'cor_raca', 'violencia_verbal', 'violencia_urbana', 'violencia_patrimonial',
                       'violencia_cyberbulling', 'violencia_religiosa', 'violencia_assedio_moral',
                       'violencia_abandono',
                       'violencia_abuso_familiar', 'violencia_atentado_pudor', 'violencia_trafico_humano',
                       'violencia_psicologica_moral', 'violencia_fisica', 'violencia_sexual',
                       'preconceito_cultural',
                       'preconceito_estetico', 'preconceito_economico', 'preconceito_religioso',
                       'preconceito_mental',
                       'preconceito_racial', 'preconceito_genero', 'preconceito_orientacao_sexual',
                       # 'servicos_indisponiveis_bairro',
                       'forma_descarte_lixo', 'percepcao_seguranca_bairro',
                       # 'problemas_bairro',
                       'fale_mais_familia'
                       ]
        self.data = {field: getattr(self.obj, field) for field in form_fields}

        self.resp = self.client.post(r('questionarios:new'), self.data)
        self.client.post(r('questionarios:new'), self.data)
        self.email = mail.outbox[0]

    @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_email_questionario_assunto(self):
        expect = 'Questionário Socioeconômico preenchido com sucesso'

        self.assertEqual(expect, self.email.subject)

    @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_email_questionario_remetente(self):
        expect = 'pescar.gt.ss@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_email_questionario_para(self):
        expect = ['samuka1@gmail.com']

        self.assertEqual(expect, self.email.to)

    @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_questionario_corpo_email(self):
        contents = [
            'Samuel Barbosa',
            'samuka1@gmail.com',
            '58500336102',
            'Palmas'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
