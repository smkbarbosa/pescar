# from unittest import skipIf
#
from django.core import mail
from django.test import TestCase
# from django_webtest import WebTest
#
from  sare.questionarios.forms import QuestionarioPessoalForm, QuestionarioEconomicoForm
# from sare.questionarios.models import Questionario
# from sare.questionarios.views import QuestionarioWizard
#
#
# class QuestionarioWizardTest(WebTest):
#     # def test_csrf(self):
#     #     """Html deve conter csrf"""
#     #     page = self.app.post('/questionario/')
#     #
#     #     form = page.form
#     #     response = form.
#     #     self.assertContains(self.resp, 'csrfmiddlewaretoken')
#     csrf_checks = False
#
#     def __init__(self, methodName='runTest'):
#         super().__init__(methodName='runTest')
#         self.request = None
#
#     def test_default(self):
#         page = self.app.post('/questionario/')
#
#         form = page.form
#         form['0-nome'] = 'Samuel Barbosa'
#         form['0-cpf'] = '12345678901'
#         form['0-email'] = 'samuka1@gmail.com'
#         form['0-cidade'] = 'Palmas'
#
#         response = form.submit().follow()
#         wizard_goto_step = self.request.POST.get('wizard_goto_step', None)
#         if wizard_goto_step and wizard_goto_step in self.get_form_list():
#             return self.render_goto_step(wizard_goto_step)
#
#         self.assertEqual(302, response.status_code)
#
#
#
class QuestionarioGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/questionario/')

    def test_get(self):
        """GET /questionario/ deve retornar status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Deve utilizar o template form_socioeconomico.html"""
        self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')

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
        self.assertIsInstance(form, QuestionarioPessoalForm)


class QuestionarioPostValid(TestCase):
    def setUp(self):
        data = {'0-nome':'Samuel Barbosa',
                '0-cpf':'12345678901',
                '0-email':'samuka1@gmail.com',
                '0-cidade':'Palmas'}

        wizard_goto_step = 1
        self.resp = self.client.post(wizard_goto_step, data)
        # self.email = mail.outbox[0]

    def test_post(self):
        """POST valid deve redirecionar to /questionario/"""
        self.assertEqual(302, self.resp.status_code)
    #
    #
    # def test_envia_email_questionario(self):
    #     pass
#         self.assertEqual(1, len(mail.outbox))
# #
# #     # @skipIf(AssertionError, "Salvar desabilitado na view")
# #     def test_salva_questionario(self):
# #         self.assertTrue(Questionario.objects.exists())
#
#
# # class QuestionarioPostInvalid(TestCase):
# #     def setUp(self):
# #         self.resp = self.client.post('/questionario/', {}) # data é um dicionário vazio
# #
# #     def test_post(self):
# #         """Post Invalid não deve redirecionar"""
# #         self.assertEqual(200, self.resp.status_code)
# #
# #     def test_template(self):
# #         self.assertTemplateUsed(self.resp, 'questionarios/form_socioeconomico.html')
# #         self.assertTemplateUsed(self.resp, 'material/includes/material_css.html')
# #         self.assertTemplateUsed(self.resp, 'material/includes/material_js.html')
# #         self.assertTemplateUsed(self.resp, 'material/form.html')
# #
# #     def test_has_form(self):
# #         form = self.resp.context['form']
# #         self.assertIsInstance(form, QuestionarioPessoalForm)
# #
# #     def test_form_has_errors(self):
# #         form = self.resp.context['form']
# #         self.assertTrue(form.errors)
# #
# #     def test_nao_salva_questionario(self):
# #        self.assertFalse(Questionario.objects.exists())
#
#
# # class QuestionarioSucessMessage(TestCase):
# #     def test_message(self):
# #         data = dict(nome='Samuel Barbosa', cpf='12345678901',
# #                     email='samuka1@gmail.com',
# #                     cidade='Palmas')
# #
# #         response = self.client.post('/questionario/', data, follow=True)
# #         self.assertContains(response, 'Questionário respondido com sucesso!')