from datetime import datetime
import random

nome_usuario = input('Digite o seu nome: ')
idade_usuario = int(input('Digite a sua idade: '))
data_registro_usuario = datetime.now().strftime('%d/%m/%Y')

cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao_usuario = random.choice(cartoes)

print(f'''Olá {nome_usuario}, seu registro foi concluido no dia {data_registro_usuario}.
Parabéns, houve um sorteio e você ganhou um cartão de compras no valror de {cartao_usuario}''')