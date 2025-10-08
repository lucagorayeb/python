def busca_menor(arr):
    n = len(arr)
    menor = arr[0]
    menor_indice = 0
    for i in range(1,n):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao_selecao(arr):
    n = len(arr)
    novoArr = []
    for j in range(n):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr
    

arr = [76,45,23,24,87,5,3,2,46]

print(ordenacao_selecao([76,45,23,24,87,5,3,2,46]))

