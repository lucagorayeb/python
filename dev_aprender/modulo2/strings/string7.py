# 8 - split e join (Separa a string e armazena em uma lista)

frase = 'Olá, bem-vindo a este treinamento'
print(frase.split()) # Por padrão o split se deixado vazio ele vai efetuar a separação nos espaços 
print(frase.split(','))
print(frase.split('-'))

hashtag = 'musica #guitarra #violão #bateria #baixo'
print(hashtag.split('#'))   
print(hashtag.split('#',3)) # Esse segundo parametro conta quantas vezes ele vai ser executado antes de parar

hashtag_separda = hashtag.split('#')
print(hashtag_separda)
print(','.join(hashtag_separda))
print('.'.join(hashtag_separda))
print(' '.join(hashtag_separda))

print('\n\n\n\n')

frase1 = 'Desafio manipulação de strings'
frase2 = 'João, Rafael, Carol, Camila'

palavras1 = frase1.split()
palavras2 = frase2.split(',')

print(','.join(palavras1))
print(' &'.join(palavras2))