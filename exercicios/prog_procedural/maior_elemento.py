def buscando_maior(arr):
    maior = 0
    for i in range(len(arr)):
        if maior < arr[i]:
            maior = arr[i]
        else:
            maior = maior
    return maior

arr = [42, 7, 19, 3, 88, 15, 1, 34, 23, 9]
print(buscando_maior(arr)) 