"""LojaGames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from games.views import home, nova_compra, novo_jogo, updateJogo, updateCompra, deleteJogo, deleteCompra

app_name='games'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('games/', include('games.urls')),
    path('compra/', nova_compra, name='url_compra'),
    path('jogo/', novo_jogo, name='url_jogo'),
    path('updateJogo/<int:pk>/', updateJogo, name='url_updateJogo'),
    path('updateCompra/<int:pk>/', updateCompra, name='url_updateCompra'),
    path('deleteJogo/<int:pk>/', deleteJogo, name='url_deleteJogo'),
    path('deleteCompra/<int:pk>/', deleteCompra, name='url_deleteCompra')
]
