from datetime import datetime

""" 
def depositar_dinheiro():
    print('Depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Depositando reais')
    
    depositando_dolar()
    depositando_reais()

depositar_dinheiro()

def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1
    elif numero == 2:
        return filho_2
    else:
        None

resultado = pai(1)
resultado() """

""" # Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

def parabenizar():
    print('Parabéns')

resultado = meu_decorator(parabenizar)
resultado() """

def meu_decorator(funcao):
    def func():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return func
# @meu_decorator -> o decorator pode ser feito assim e não precisa das linhas resultado
@meu_decorator
def baixar_musica():
    print('Baixando música')

baixar_musica()

""" resultado = meu_decorator(baixar_musica)
resultado() """

