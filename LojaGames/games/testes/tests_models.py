from django.test import TestCase
from ..models import Jogo
# Create your tests here.

class test_jogo(TestCase):
    
    def setUp(self):
        Jogo.objects.create(
            nome="Mass Effect",
            genero="RPG"
        )

    def test_retorno_str(self):
        t1 = Jogo.objects.get(nome='Mass Effect')
        self.assertEquals(t1.__str__(), 'Mass Effect')
