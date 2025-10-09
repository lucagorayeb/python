# Refatoração
# F2 -> Para renomear todas as ocorrências
class Calculadora:
    pass

calc1 = Calculadora()
calc2 = Calculadora()
calc3 = Calculadora()

print(calc1)

# Extrair uma função com o ctrl + shift + p e escolhemos o python refactor extrair metodo
def adicao():
    resultado = 20 + 50

adicao()

# Extrair uma variavel com o ctrl + shift + p e escolhemos o python refactor extrair variavel
altura = 60
largura = 2
tamanho = (altura/largura) + 50
