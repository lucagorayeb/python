# Filter me retorna tudo aqui que é verdadeiro

""" nomes = ['Larissa', 'Rafael', 'Marcus', 'john']

def pessoa_aprovada(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False

print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897 ]
]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas))) """

vagas = [
    ['Vaga 1', 1200 ],
    ['Vaga 2', 2550 ],
    ['Vaga 3', 5000 ]
]

def maior_2500(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False

print(list(filter(maior_2500, vagas)))
print(list(map(maior_2500, vagas)))
