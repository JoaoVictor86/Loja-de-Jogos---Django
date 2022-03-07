from django.test import TestCase

from games.form import JogoForm

class JogoFormTestCase(TestCase):

    def test_jogo_form_valido_1(self):
        form = JogoForm(data={
            'nome': 'Mass Effect',
            'genero': 'RPG'
        })
        self.assertTrue(form.is_valid())
    
    def test_jogo_form_valido_2(self):
        form = JogoForm(data={
            'nome': 'Call of Duty',
            'genero': 'FPS'
        })
        self.assertTrue(form.is_valid())

    def test_jogo_form_valido_3(self):
        form = JogoForm(data={
            'nome': 'Age of Mythology',
            'genero': 'Estratégia'
        })
        self.assertTrue(form.is_valid())