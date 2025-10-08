teclado = 'Teclado'

print(teclado[-1]) # Imprime a letra que está nessa posição
print(teclado.index('l'))# Imprime a posição que está essa letra
print(teclado[teclado.index('l')])
print(teclado[0:4]) # Imprime as letras dessa posição até a próxima

frase = 'Clean Code'
print(frase.rindex('C'))

biblioteca = 'Biblioteca'

print(biblioteca.index(biblioteca[biblioteca.index('o')]))

frase2 = 'Desenvolvimento De Aplicações'

print(frase2[frase2.rindex('D') : frase2.rindex('s')])