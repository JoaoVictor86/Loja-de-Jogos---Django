from cgitb import html
from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from .models import Jogo, Compra
from .form import CompraForm, JogoForm

# Create your views here.

def home(request):
    data = {}
    data['jogos'] = Jogo.objects.all()
    data['compras'] = Compra.objects.all()
    
    return render(request, 'games/home.html', data)

def nova_compra(request):
    data = {}
    form = CompraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    return render(request, 'games/comprar.html', data)

def novo_jogo(request):
    data = {}
    form = JogoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    return render(request, 'games/jogo.html', data)