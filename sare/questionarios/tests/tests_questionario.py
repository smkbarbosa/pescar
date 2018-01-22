from django.test import TestCase
from  sare.questionarios.forms import QuestionarioForm


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
                ('<div', 624),
                ('<input', 251),
                ('<label', 300),
                ('type="text"', 22),
                ('type="checkbox"', 18),
                ('type="radio"', 207),
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
        self.assertIsInstance(form, QuestionarioForm)



