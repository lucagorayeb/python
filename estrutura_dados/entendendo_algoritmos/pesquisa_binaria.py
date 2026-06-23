#!/usr/bin/env python3
# A pesquisa binária é um algoritmo que faz buscas com o tempo de execução
# log N na base 2, o que torna ela bem rápida.

import random

def pesquisa_binaria(array, item):
    baixo = 0 
    alto = len(array) - 1

    while baixo <= alto:
        meio = int((baixo + alto)/2)
        chute = array[meio]

        if chute == item:
            return f"Parabéns você acertou. O número era {chute}"
        
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
            
    
    return None


array = [1,2,3,4,5,6,7,8,9,10]
print(pesquisa_binaria(array, -1))

