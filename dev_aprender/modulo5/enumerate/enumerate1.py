# Enumerate permite saber qual o indice que estamos buscando
""" for indice,numero in enumerate(range(1,11),1):
    print(indice,numero)
    if indice == 5:
        print('Estamos na metade da lista')

nomes = ['nome1', 'nome2', 'nome3', 'nome4', 'nome5']

for indice,nome in enumerate(nomes,1):
    print(indice,nome)
    if indice == 3:
        print('Já temos 3 pessoas cadastradas') """

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']
for indice,fruta in enumerate(frutas): 
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice,fruta)