# Set -> Exclui duplicatas 

numeros = [2, 2, 5, 6]
frutas = ['maça', 'banana', 'uva', 'maça', 'morango']

# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

print(set_numeros)
print(set_frutas)

# Adicionando novos valores
set_numeros.add(10)
print(set_numeros)

# Conjuntos
numeros1 = [2,2,5,8]
numeros2 = [2,2,3,9]

a = set(numeros1)
b = set(numeros2)

print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))
