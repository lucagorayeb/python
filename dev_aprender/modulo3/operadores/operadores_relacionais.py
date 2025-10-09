""" # Vamos pensar no seguinte exemplo 
idade = 21
possui_convite = False
filho_do_dono = True
print(idade >= 21 and possui_convite == True)
print(idade >= 21 or possui_convite == True)

# Maior de 21 anos e possui o convite ou seja filho do dono
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

# Exemplo 
maior_de_idade = True 
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

# Você só pode trabalhar aqui se for maior de idade e passuir carteira de trabalho 
print(possui_carteira_de_trabalho == True and maior_de_idade == True)
print(possui_carteira_de_trabalho and maior_de_idade)

# Queremos contratar pessoas que não possuem veículo próprio, mas já possuam carteira de trabalho  
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio) """

possui_passaporte = False 
passagem_comprada = False 
menor_de_idade = False

print((possui_passaporte and passagem_comprada) and not menor_de_idade)
print((possui_passaporte or passagem_comprada) and not menor_de_idade)
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)
print((possui_passaporte or passagem_comprada) and not menor_de_idade)