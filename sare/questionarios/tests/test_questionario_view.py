from unittest import skipIf

from django.core import mail
from django.test import TestCase
from  sare.questionarios.forms import QuestionarioPessoalForm, QuestionarioEconomicoForm
from sare.questionarios.models import Questionario
from sare.questionarios.views import QuestionarioWizard


class QuestionarioGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/questionario/')

    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve usar questionario/form_socioeconomico.html"""
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')

    def test_html(self):
        """Html deve conter input tags"""
        tags = (('<form', 1),
                # ('<div', 631),
                # ('<input', 252),
                # ('<label', 301),
                # ('type="text"', 22),
                # ('type="checkbox"', 18),
                # ('type="radio"', 207),
                ('type="submit"', 1),
                )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioPessoalForm)

    def test_has_wizard_form(self):
        wizard = self.resp.context['wizard']
        self.assertIsInstance(wizard, QuestionarioWizard)


class QuestionarioPostValid(TestCase):
    def setUp(self):
        data = dict(nome='Samuel Barbosa', cpf='12345678901',
                    email='samuka1@gmail.com',
                    cidade='Palmas')
        self.resp = self.client.post('/questionario/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """POST valid deve redirecionar to /questionario/"""
        self.assertEqual(302, self.resp.status_code)

    def test_envia_email_questionario(self):
        self.assertEqual(1, len(mail.outbox))

    # @skipIf(AssertionError, "Salvar desabilitado na view")
    def test_salva_questionario(self):
        self.assertTrue(Questionario.objects.exists())


class QuestionarioPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/questionario/', {}) # data é um dicionário vazio

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
        self.assertIsInstance(form, QuestionarioPessoalForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_nao_salva_questionario(self):
       self.assertFalse(Questionario.objects.exists())


class QuestionarioSucessMessage(TestCase):
    def test_message(self):
        data = dict(nome='Samuel Barbosa', cpf='12345678901',
                    email='samuka1@gmail.com',
                    cidade='Palmas')

        response = self.client.post('/questionario/', data, follow=True)
        self.assertContains(response, 'Questionário respondido com sucesso!')