from unittest import skip, skipIf

from django.core import mail
from django.forms import model_to_dict
from django.shortcuts import resolve_url as r
from django.test import TestCase
from model_mommy import mommy

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


class QuestionarioNovoGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('questionarios:new'))

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    # def test_template(self):
    #     """Deve utilizar o template form_socioeconomico.html"""
    #     self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_html(self):
        """HTML deve conter algumas tags específicas"""
        tags = (('<form', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)


class QuestionarioNovoPost(TestCase):
    def setUp(self):
        # self.obj = mommy.prepare_recipe('sare.questionarios.quest', _fill_optional=True, _save_related=True)

        self.obj = mommy.prepare(Questionario, nome='Samuel Barbosa', cpf='85472840519', email='samuka1@gmail.com',
                                 cidade='Palmas', bairro='Plano Diretor norte', origem_renda='2',
                                 fale_mais_familia='OK Teste', _fill_optional=True)

        form_fields = model_to_dict(self.obj, fields=[field.name for field in self.obj._meta.fields])

        data = {field: getattr(self.obj, field) for field in form_fields}

        self.resp = self.client.post(r('questionarios:new'), data)
        self.uuid = Questionario.objects.first().hashId
        self.email = mail.outbox[0]

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_post(self):
        """POST valid deve redirecionar to /questionario/00000000-0000-0000-0000-000000000000/"""
        self.assertRedirects(self.resp, r('questionarios:detalhe', self.uuid))

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_salva_questionario(self):
        self.assertTrue(Questionario.objects.exists())


class QuestionarioNovoPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('questionarios:new'), {})  # data é um dicionário vazio

    # @skipIf('ERROR','Pulando enquanto o redirecionamento for para consultar')
    def test_post(self):
        """Post Invalid não deve redirecionar"""
        self.assertEqual(200, self.resp.status_code)

    # @skipIf('ERROR','Pulando enquanto o redirecionamento for para consultar')
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_css.html')
        self.assertTemplateUsed(self.resp, 'material/includes/material_js.html')
        self.assertTemplateUsed(self.resp, 'material/form.html')

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    # @skipIf('ERROR', 'Pulando enquanto o redirecionamento for para consultar')
    def test_nao_salva_questionario(self):
        self.assertFalse(Questionario.objects.exists())
