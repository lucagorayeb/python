# Caso a idade seja maiot ou igual a 18 anos, essa pessoa é maior de idade, caso contrário ela é menor de idade

""" idade = 15 
if idade >= 18:
    print('Maior de idade')
else: 
    print('Menor de idade') """

idade = 15 
print("Maior de idade") if idade >= 18 else print('Menor de idade')

possui_passaporte = False

print('Favor embacar') if possui_passaporte else print('Favor tirar passaporte')

velocidade = 80
print('você foi multado') if velocidade >= 100 else print('Não foi multado')