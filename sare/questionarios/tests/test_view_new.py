from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

from sare.questionarios.forms import QuestionarioForm
from sare.questionarios.models import Questionario


class QuestionarioGet(TestCase):
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


class QuestionarioPostValid(TestCase):
    def setUp(self):
        data = {'nome':'Samuel Barbosa',
                'cpf':'12345678901',
                'email':'samuka1@gmail.com',
                'cidade':'Palmas',
                'condicao_responsavel_casa':'1',
                'meio_acesso_campus':'1',
                'condicao_moradia':'5',
                'local_moradia':'1',
                'total_pessoas_casa':'2',
                'total_comodos_casa':'3',
                'total_km_casa_campus':'2',
                'instituicao_anterior':'6'
        }

        self.resp = self.client.post(r('questionarios:new'), data)
        self.id = Questionario.objects.first().id  # agregado
        self.email = mail.outbox[0]

    def test_post(self):
        """POST valid deve redirecionar to /questionario/1/"""
        self.assertRedirects(self.resp, r('questionarios:detalhe', '11111111-1111-1111-1111-111111111111'))

    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

#
#     # @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_salva_questionario(self):
        self.assertTrue(Questionario.objects.exists())


class QuestionarioPostInvalid(TestCase):
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
