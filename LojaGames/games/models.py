from tabnanny import verbose
from django.db import models

# Create your models here.


class Jogo(models.Model):
    nome = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data = models.DateTimeField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    observacoes = models.TextField(null=True, blank=True)

    
