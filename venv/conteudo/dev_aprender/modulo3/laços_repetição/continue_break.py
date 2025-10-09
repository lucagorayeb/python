# Continue, ignorar/pular

for numero in range(10):
    if numero % 2 == 0:
        print(numero)
    else:
        continue


# Break, para interronperm a iteração
for numero in range(10):
    if numero % 2 == 0:
        print(numero)
    else:
        break

estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']

for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)

for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)