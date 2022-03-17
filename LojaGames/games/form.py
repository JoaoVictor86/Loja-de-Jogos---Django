from attr import fields
from django.forms import ModelForm
from .models import Compra, Jogo

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['jogo', 'data', 'valor', 'observacoes']

class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome', 'genero']

