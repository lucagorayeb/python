

vet = [2,4,6,8]

def contagem(vet):
        if  vet == []:
            return 0
        else:
            vet.pop(0)
            return 1 + contagem(vet)

print(contagem(vet)) 

