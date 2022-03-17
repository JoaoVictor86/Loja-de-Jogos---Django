from unicodedata import name
from . import views
from django.urls.conf import path
from django.contrib import admin

app_name='games'

urlpatterns=[
    path('', views.novo_jogo, name='url_jogo'),
    path('deleteJogo/<int:pk>/', views.deleteJogo, name='url_deleteJogo')
]