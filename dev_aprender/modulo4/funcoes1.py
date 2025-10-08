# Funções

""" input()
len()
 São todas funções
 """

# Para criar uma função
# def nome_da_função(parametro):
#    comandos

""" def dar_boas_vindas():
    print('Bem vindo')

dar_boas_vindas()

def dar_boas_vindas_personalizada(nome):
    print(f'Bem vindo {nome}')

dar_boas_vindas_personalizada('Luca')

def apresenta_lugar(lugar = 'Dysney'):
    print(f'Conheça a {lugar}')

apresenta_lugar()

def apresenta_lugar2(horario_funcionamento, lugar = 'Dysney'):
    print(f'Conheça a {lugar} que funciona das {horario_funcionamento}')

apresenta_lugar2('8h as 18h')
 """

def gerar_nome_completo(nome):
    print(f'Bem vindo(a) {nome}')

nome = input("Qual o seu nome completo? ")
gerar_nome_completo(nome)

def calcular_valores(preco, quantidade = 7):
    print(preco*quantidade)

calcular_valores(4.99)
