# Dictionary compreheension 
# [expressão for menbro in iterável]
# {chave:expressão for menbro in iterável}
from pprint import pprint
pprint({i: i for i in range(20)})

# Popular um dicionário com valores
produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
pprint({produto: 1 for produto in produtos})

# Gerar uma matriz de valores de teste
# [expressão for membro in iterável]
pprint({produto: [0 for i in range(5)] for produto in produtos})
# Mais robusto 
pprint({produto: [2 * i for i in range(5)] for produto in produtos})
# Gerar valores de teste
import random 
pprint({produto: [random.randint(1000,15000) for i in range(5)] for produto in produtos})

# Desafio 1
sorteios = ['sorteio 1', 'sorteio 2','sorteio 3']
participantes = ['Joel', 'Jessica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'Jhon']
pprint({sorteio:[random.choice(participantes) for i in range(1)] for sorteio in sorteios})

# Desafio 2
grupos = ['grupo 1', 'grupo 2', 'grupo 3']
pprint({grupo:[random.randint(1,100) for i in range(5)]for grupo in grupos})
