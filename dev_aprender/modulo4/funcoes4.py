# *args receber uma quantidade variada de argumentos posicionais

""" def somar(*valores,b): # valores ficam com formato de tupla(lista) *args
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 45, 5, b = 6) """

# kwargs (Keyword arguments)

""" def concatenar(**palavras): # Consigo receber ilimitada de argumentos nomeados
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a = 'Nós', b = 'Somos', c = 'Pythonistas', d = 'Profissionais') """

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)

    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Luca',4,5,6,7,a=1,b=2,c=3)