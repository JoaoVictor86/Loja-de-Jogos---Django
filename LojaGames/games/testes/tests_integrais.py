from django.urls import reverse
import pytest
from ..models import Jogo
from django.test import Client

#Framework utilizado: Pytest
#Comando para executar os testes: pytest games/testes/tests_integrais.py

@pytest.fixture
def adicionar_jogo(client, db):
    resp = client.post(reverse('games:url_jogo'), data={'nome':'Jogo 1', 'genero':'RPG'})
    return resp

@pytest.mark.django_db
def test_jogo_existe_no_bd(adicionar_jogo):
    assert Jogo.objects.exists()

@pytest.mark.django_db
def test_redirecionamento_depois_do_salvamento(adicionar_jogo):
    assert adicionar_jogo.status_code == 302

@pytest.fixture
def jogo2(db):
    return Jogo.objects.create(nome='Jogo 2', genero='FPS')

@pytest.fixture
def apagar_jogo(client, jogo2):
    resp = client.post(
        reverse('games:url_deleteJogo', kwargs={'pk':jogo2.id})
    )
    return resp

@pytest.mark.django_db
def test_apagar_jogo(apagar_jogo):
    assert not Jogo.objects.exists()

@pytest.mark.django_db
def test_redirecionamento_depois_da_exclusao(apagar_jogo):
    assert apagar_jogo.status_code == 302