# Como podemos criar listas?
# Criar listas usando Loops e Range()
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Map
nomes = ['Larissa', 'Rafael', 'Marcus', 'john']

def aprovar_pessoa(nome):
    return nome + ' Aprovado'

print(list(map(aprovar_pessoa, nomes)))