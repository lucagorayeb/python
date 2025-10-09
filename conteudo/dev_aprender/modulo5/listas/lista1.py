preco_1 = 10
preco_2 = 20
preco_3 = 30

# Listas
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 47, 784, 28, 3, 672]
print(precos[0]) # Indice
print(precos[precos.index(100)])

# Listas no Python são dinâmicas (aceitam qualquer tipo de dado) 
itens = [1,3,6, 'Olá', 'Café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista 
# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10 
lista_de_testes = ['Teste'] * 10
print(lista_de_noves)
print(lista_de_testes) 

# Usando o gerador range(sequência)
# 1 a 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de strings 
print(list('Bem vindo ao treinamento'))

# Lista de uma lista(matriz)
matriz_de_nome_idade = [['Carol',30],['Marcos', 50]]
print(matriz_de_nome_idade[0])
print(matriz_de_nome_idade[0][0])

lista_do_desafio = ['Computador', 'Celular', 'Copo']# Desafio 1

lista_de_range = list(range(10,132))# Desafio 2

print(lista_do_desafio + lista_de_range)# Desafio 3

matriz_desafio = [['Computador', 10000.00], ['Celular', 4000.00], ['Copo', 20.00]] # Desafio 4
print(matriz_desafio[0])
