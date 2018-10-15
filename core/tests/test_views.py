from django.test import SimpleTestCase
from django.urls import reverse

class CoreViewsTest(SimpleTestCase):

    def test_index_status_200(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'index.html')

    def test_index_status_200_pelo_nome(self):
        response = self.client.get(reverse("core:home"))
        self.assertTemplateUsed(response, 'index.html')

    def test_contato_status_200(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'contato.html')

    def test_contato_status_200_pelo_nome(self):
        response = self.client.get(reverse("core:contato"))
        self.assertTemplateUsed(response, 'contato.html')
