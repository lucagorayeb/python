""" trabalho_terminado = False

if trabalho_terminado == True:
    print("Bora dar um saída")
else:
    print('Não, não posso sair agora')


numero_atrasos = 2

if numero_atrasos >=3:
    print('vá para a diretoria')
elif numero_atrasos == 2:
    print('Essa é sua segunda falta')
elif numero_atrasos == 1:
    print('Essa é sua segunda falta')
else:
    print('Pode entrar') 

# Chaining
velocidade_carro = 30

if velocidade_carro <= 50:
    print('Não levou multa')
# elif velocidade_carro >= 51 and velocidade_carro <= 60:
elif 51 <= velocidade_carro <= 60: # Chaining
    print('Lwvou multa de dois pontos')
elif velocidade_carro >= 61 and velocidade_carro <= 75:
    print('Levou multa de tres pontos')
else:
    print('Levou multa de sete pontos') """

# Valor do corte de cabelo 

tamanho_cabelo = 56

if tamanho_cabelo <= 20:
    print('Valor é R$50,00')
elif 21 <= tamanho_cabelo <=30:
    print('Valor é R$70,00')
elif 31 <= tamanho_cabelo <=50:
    print('Valor é R$100,00')
else:
    print('Favor consultar na recepção')