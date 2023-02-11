from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(requisicao):
    return render(requisicao, 'receita/pages/home.html', context={'meu_dict': 'sou uma variavel'})


def sobre(requisicao):
    return render(requisicao, 'receita/pages/about.html', context={'meu_dict': 'sou uma variavel'})


def contato(requisicao):
    return render(requisicao, 'receita/pages/contact.html', context={'meu_dict': 'sou uma variavel'})
