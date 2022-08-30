from django.test import TestCase
from django.urls import reverse


class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Loja Virtual')

    def testar_se_pagina_ajuda_carrega_completamente(self):
        response = self.client.get(reverse("ajuda"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Ajuda')

