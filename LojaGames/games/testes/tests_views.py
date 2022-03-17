from django.test import TestCase
from django.urls import reverse

#Framework utilizado: TestCase do Django
#Comando para testar os testes unitários: python manage.py test games

class JogoViewTestCase(TestCase):

    def test_status_code_200_home(self):
        response = self.client.get(reverse('url_home'))
        self.assertEquals(response.status_code, 200)
    
    def test_status_code_200_compra(self):
        response = self.client.get(reverse('url_compra'))
        self.assertEquals(response.status_code, 200)

    def test_status_code_200_jogo(self):
        response = self.client.get(reverse('url_jogo'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado_home(self):
        response = self.client.get(reverse('url_home'))
        self.assertTemplateUsed(response, 'games/home.html')

    def test_template_usado_compra(self):
        response = self.client.get(reverse('url_compra'))
        self.assertTemplateUsed(response, 'games/comprar.html')
    
    def test_template_usado(self):
        response = self.client.get(reverse('url_jogo'))
        self.assertTemplateUsed(response, 'games/jogo.html')