from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def contato(request):
    return HttpResponse('Contatos')

def minha_historia(request):
    return render(request,'investimentos/minha_historia.html')