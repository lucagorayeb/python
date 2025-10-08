# Ordenar por propriedade
from operator import itemgetter

""" nomes = ['Zack', 'Camilla', 'Julius', 'Romer']
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 28]
nomes.sort()
print(nomes)
valores.sort()
print(valores)

pessoas = [
    {
        'nome': 'Luca',
        'idade': 19,
        'nível de acesso': 5
    },

    {
        'nome': 'Larissa',
        'idade': 20,
        'nível de acesso': 1
    },

    {
        'nome': 'João',
        'idade': 31,
        'nível de acesso': 3
    },

    {
        'nome': 'Maria',
        'idade': 45,
        'nível de acesso': 2
    }
]

pessoas.sort(key = itemgetter('nome'))
print(pessoas)

produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]

produtos.sort(key = itemgetter(0), reverse = True)
print(produtos)

matriz = [[5, 10], [15, 20], [1, 5]]
matriz.sort(key=itemgetter(1))
print(matriz) """

# Desafio 1

produtos = [
    {
        'nome': 'Celular',
        'preco': 1500
    },

    {
        'nome': 'Monitor',
        'preco': 500
    },

    {
        'nome': 'Microfone',
        'preco': 300
    }
]

produtos.sort(key = itemgetter('preco'))
print(produtos)

# Desafio 2

equipamento_filmagem = [
    ('Tripé', 300),
    ('câmera', 1700),
    ('Iluminação', 200)
]

equipamento_filmagem.sort(key = itemgetter(1), reverse = True)
print(equipamento_filmagem)

# Desafio 3

cotacao_moedas = [['usd', 6.00], ['brl', 1.50], ['eur', 7.20]]
cotacao_moedas.sort(key = itemgetter(1))
print(cotacao_moedas)
