from django.test import TestCase
from  sare.questionarios.forms import QuestionarioForm


class QuestionarioTest(TestCase):
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
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<fieldset', 54 )
        self.assertContains(self.resp, '<legend', 53)
        self.assertContains(self.resp, '<p', 5)
        self.assertContains(self.resp, '<div', 195)
        self.assertContains(self.resp, '<input', 256)
        self.assertContains(self.resp, '<label', 242)
        self.assertContains(self.resp, 'type="text"', 9)
        self.assertContains(self.resp, 'type="checkbox"', 35)
        self.assertContains(self.resp, 'type="radio"', 207)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html deve conter csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context deve ter form de questionario"""
        form = self.resp.context['form']
        self.assertIsInstance(form, QuestionarioForm)

    def test_form_has_fields(self):
        """Form deve conter campos """
        form = self.resp.context['form']
        self.assertSequenceEqual(['nome', 'cpf', 'sexo','dependentes_RBD', 'origem_renda', 'renda_bruta_domiciliar'  ], list(form.fields))
