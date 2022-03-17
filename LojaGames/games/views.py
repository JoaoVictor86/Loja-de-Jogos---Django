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

def updateJogo(request, pk):
    data = {}
    jogo = Jogo.objects.get(pk=pk)
    form = JogoForm(request.POST or None, instance=jogo)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    data['jogo'] = jogo
    return render(request, 'games/jogo.html', data)

def updateCompra(request, pk):
    data = {}
    compra = Compra.objects.get(pk=pk)
    form = CompraForm(request.POST or None, instance=compra)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    
    data['form'] = form
    data['compra'] = compra
    return render(request, 'games/comprar.html', data)

def deleteJogo(request, pk):
    jogo = Jogo.objects.get(pk=pk)
    jogo.delete()
    return redirect('url_home')

def deleteCompra(request, pk):
    compra = Compra.objects.get(pk=pk)
    compra.delete()
    return redirect('url_home')