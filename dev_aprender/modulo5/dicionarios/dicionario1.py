# Dicionários 

""" 
    Pessoa
        nome
        idade
        altura
"""
# Dicionário(chave, valor)
dicionario_pessoa = {'nome':'Luca','idade':19,'altura':1.60}
print(dicionario_pessoa)


#pessoa = dict(nome = 'Luca', idade = 19, altura = 1.70)

print(dicionario_pessoa.keys())# Apenas chaves
print(dicionario_pessoa.values())# Apenas valores
print(dicionario_pessoa.items())# Ambos 

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])