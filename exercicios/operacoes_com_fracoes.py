def soma_fracao(n1, d1, n2, d2):
    numerador = (n1*d2 + n2*d1)
    denominador = (d1*d2)
    return simplifica_fracao(numerador, denominador)

def subtracao_fracao(n1, d1, n2, d2):
    numerador = (n1*d2 - n2*d1)
    denominador = (d1*d2)
    return simplifica_fracao(numerador, denominador)

def multiplicacao_fracao(n1, d1, n2, d2):
    numerador = (n1*n2)
    denominador = (d1*d2)
    return simplifica_fracao(numerador, denominador)

def divisao_fracao(n1, d1, n2, d2):
    numerador = (n1*d2)
    denominador = (d1*n2)
    return simplifica_fracao(numerador, denominador)
    

def simplifica_fracao(numerador, denominador):
    while ((numerador % 3 == 0 and denominador % 3 == 0) or (numerador % 2 == 0 and denominador % 2== 0)):
        if numerador % 2 == 0 and denominador % 2 == 0:
            numerador = numerador / 2
            denominador = denominador / 2
            fracao = f'{numerador}/{denominador}'
        elif numerador % 3 == 0 and denominador % 3 == 0:
            numerador = numerador / 3
            denominador = denominador / 3
            fracao = f'{numerador}/{denominador}'
        else: 
            None      
    return fracao

def chama_operacao(n1, d1, operador, n2, d2):
    if operador == '+':
        return soma_fracao(n1, d1, n2, d2)
    elif operador == '-':
        return subtracao_fracao(n1, d1, n2, d2)
    elif operador == '*':
        return multiplicacao_fracao(n1, d1, n2, d2)
    elif operador == '/':
        return divisao_fracao(n1, d1, n2, d2)

def transforma_string_em_int_e_armazena_no_vetor(fracoes):
    num = fracoes.split()
    return chama_operacao(int(num[0]), int(num[2]), num[3], int(num[4]), int(num[6])
)



fracao = input('Digite a operação com frações que você quer realizar? ')
print(transforma_string_em_int_e_armazena_no_vetor(fracao))




    
    