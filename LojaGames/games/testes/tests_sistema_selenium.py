from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Framework utilizado: TestCase do Django
#Comando para testar os testes de sistema: python manage.py test games

class JogoFormTest(LiveServerTestCase):
  
  def test_jogo_form(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/jogo')

        jogo_nome = selenium.find_element_by_id('id_nome')
        jogo_genero = selenium.find_element_by_id('id_genero')

        submit = selenium.find_element_by_id('submit_button')

        jogo_nome.send_keys('Dark Souls')
        jogo_genero.send_keys('RPG')

        submit.send_keys(Keys.RETURN)

        assert 'Dark Souls' in selenium.page_source

class CompraFormTest(LiveServerTestCase):
  
  def test_compra_form(self):
        selenium = webdriver.Chrome()
        selenium.get('http://127.0.0.1:8000/compra')

        compra_jogo = selenium.find_element_by_id('id_jogo')
        compra_data = selenium.find_element_by_id('id_data')
        compra_valor = selenium.find_element_by_id('id_valor')

        submit = selenium.find_element_by_id('submit_button')

        compra_jogo.send_keys('Skyrim')
        compra_data.send_keys('2022-03-24 14:55:00')
        compra_valor.send_keys('30')

        submit.send_keys(Keys.RETURN)

        assert 'Skyrim' in selenium.page_source