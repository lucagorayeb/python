# Retorna o erro que aconteceu
try:
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um índice válido') 
    print(erro)


internet = None
try:
    print('Fazendo conexão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')

try:
    valor = int(input('Digite um valor: '))
    print(valor/0)
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero!')
except ValueError as erro:
    print('Favor digitar apenas número')
finally:
    print('Operação cancelada')