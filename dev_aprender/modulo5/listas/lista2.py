valores = [1, 2, 3, 4, 2, 5, 6, 7, 8, 9, 10]
anos = [2020, 2030, 2040, 2050]

# Adicionar ao final da lista
valores.append(11)
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

# Adicionar listas
nova_lista = valores + anos
print(nova_lista)

# Inserir um novo valor
print(anos[1])
anos.insert(2,2031)
print(anos)

# Extrair com base no índice
anos_2020 = anos.pop(0)
print(anos_2020)

# Remover o item da lista
anos.remove(2050)
print(anos)
""" del anos[0:2]
print(anos) -> Serve para remover um faixa de valores """

# Contando a ocorrência de um valor 
print(valores.count(2))


# Exluir todos os itens de uma lista
anos.clear()
print(anos)