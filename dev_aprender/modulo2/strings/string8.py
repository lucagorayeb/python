# Recebendo dados do usuário

# Todo dado recebido de input é caracterizado como string por padrão 
senha = input('Digite a sua senha: ')
print(senha)
print(type(senha))

# Se passamos o tipo da variavel antes do input vai retornar o tipo correto
quantidade_de_filmes = int(input('Quantos filmes você viu este ano?'))
print(type(quantidade_de_filmes))