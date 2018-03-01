from unittest import skipIf

import django
from django.core import mail
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.shortcuts import resolve_url as r
from model_mommy import mommy

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


class QuestionarioNovoGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('questionarios:new'))

    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    # def test_template(self):
    #     """Deve utilizar o template form_socioeconomico.html"""
    #     self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')

    def test_html(self):
        """HTML deve conter algumas tags específicas"""
        tags = (('<form', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)


class QuestionarioNovoPost(TestCase):
    def setUp(self):
        # self.obj = mommy.prepare_recipe('sare.questionarios.quest', _fill_optional=True, _save_related=True)

        self.obj = mommy.prepare(Questionario, nome='Samuel Barbosa', cpf='31882451309', email='samuka1@gmail.com',
                                  cidade='Palmas', bairro='Plano Diretor norte', origem_renda='2',
                                  fale_mais_familia='OK Teste', _fill_optional=True)

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

        data = {field: getattr(self.obj, field) for field in form_fields}


        self.resp = self.client.post(r('questionarios:new'), data)
        self.uuid = Questionario.objects.first().hashId
        self.email = mail.outbox[0]

    # @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_post(self):
        """POST valid deve redirecionar to /questionario/00000000-0000-0000-0000-000000000000/"""
        self.assertRedirects(self.resp, r('questionarios:detalhe', self.uuid))

    # @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

    #
    # @skipIf(AssertionError, "desabilitado ate resolver como passar o teste com unique_together")
    def test_salva_questionario(self):
        self.assertTrue(Questionario.objects.exists())


class QuestionarioNovoPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('questionarios:new'), {})  # data é um dicionário vazio

    def test_post(self):
        """Post Invalid não deve redirecionar"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_css.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_js.html')
        self.assertTemplateUsed(self.resp, 'material/form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_nao_salva_questionario(self):
        self.assertFalse(Questionario.objects.exists())
