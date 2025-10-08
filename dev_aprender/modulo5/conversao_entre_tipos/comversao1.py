# Conversão de tipos 

idade = input('Digite a sua idade:')
print(int(idade) > 17)

ano_publicacao = 2020
print('Este livro foi criado em' + str(ano_publicacao))

altura = input('Altura da parede?')
print(float(altura) > 2.50)

# Converções entre coleções

saudacao = 'Hello!'

print(list(saudacao))
print(set(saudacao))
print(tuple(saudacao))
print(list(range(30)))