from django.test import TestCase


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
        """Html deve conter iframe tags"""
        self.assertContains(self.resp, '<iframe')
