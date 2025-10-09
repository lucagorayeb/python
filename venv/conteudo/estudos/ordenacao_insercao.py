def ordenacao_insercao(arr):
    n = len(arr)
    for j in range(n):
        chave = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > chave:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = chave
        



arr = [42, 7, 19, 3, 88, 15, 1, 27]
ordenacao_insercao(arr)
print("Array ordenado:", arr)

