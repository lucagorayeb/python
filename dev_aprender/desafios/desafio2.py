from turtle import Turtle
# Inicializando uma turtle 
t = Turtle()

# Definir a velocidade 
t.speed(1)

# Condicional de perguntas (frente e trás)
    # > Receber os pixels

# Condicional de perguntas (Esquerda ou direita)
    # > Receber os pixels

def movimentar_tartaruga():
    movimento = input('Você quer andar para frente ou para trás? ')

    if movimento == 'frente' or movimento == 'Frente':
        quantidade = pixels_para_movimentar()
        t.forward(quantidade)
    elif movimento == 'Trás' or movimento == 'trás':
        quantidade = pixels_para_movimentar()
        t.back(quantidade)


def rotacionar_tartaruga():
    rotacao = input('Você quer rotacionar para a esquerda ou para a direita? ')

    if rotacao == 'esquerda' or rotacao == 'Esquerda':
        quantidade = pixels_para_movimentar()
        t.left(quantidade)
    elif rotacao == 'direita' or rotacao == 'Direita':
        quantidade = pixels_para_movimentar()
        t.right(quantidade)

def continuar_movimentado_tartaruga():
    continuar_andando = input("Você quer continuar andando? ")

    if continuar_andando == 'sim' or continuar_andando == 'Sim':
        return True
    elif continuar_andando == 'não' or continuar_andando == 'Não' or continuar_andando == 'nao' or continuar_andando == 'Nao':
        return False


def pixels_para_movimentar():
    pixels = int(input('Quantos pixels? '))
    return pixels
    
resultado = True
while resultado != False:
    movimentar_tartaruga()
    rotacionar_tartaruga()
    resultado = continuar_movimentado_tartaruga()



