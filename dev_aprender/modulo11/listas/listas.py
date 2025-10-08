# Como podemos criar listas?

# Criar listas usando Loops e Range()
""" numeros = []
for i in range(5):
    numeros.append(i)
print (numeros)"""

# Map 
nomes = ['Larissa', 'Luca', 'João', 'Maria'] 

def aprovar_pessoa(nome):
    return nome + " APROVADO"

# print(list(map(aprovar_pessoa, nomes)))

# Como usar uma list compreheension 
nova_lista =  [2 * i for i in range(10)]
# [expressao for menbro in iterável]
print(nova_lista)

# print([nome + " APROVADO" for nome in nomes])
print([aprovar_pessoa(nome) for nome in nomes])


# Fazendo uma matriz 
from pprint import pprint
pprint([[i for i in range(1,6)] for x in range(5)])

# Usar condicionais em list compreheesion
# [expressão for membro in iterável (condicional if)]
print([aprovar_pessoa(nome) for nome in nomes if nome != 'João'])

# Valores numéricos 
def numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False
    
print([i for i in range(20) if numero_par(i)])

# A condicional é flexível 
# [expressão (condicional if) for menbro in iterável]
participantes = ['Zé', 'Felipe', 'Marcos', 'Vitor']
ganhadores = ['Felipe', 'Marcos']

print([i + ' GANHADOR' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes ])

# Desafio 1
print([i for i in range(1,11) if numero_par(i)])

# Desafio 2
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'rosa', 'preto']
pprint([ str(cores.index(i)+1) + ' - ' + i for i in cores])

# Desafio 3 
participantes = ['Joel', 'Jessica', 'Maria', 'Cris', 'Larissa', 'Rafael', 'Marcus', 'Jhon']
pagamento_realizado = ['Joel', 'Jessica', 'Maria', 'Cris']
print([i + ' PAGO' if i in pagamento_realizado else i for i in participantes ])