def quicksort(arr):
    if len(arr) <= 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

arr = [9, 3, 7, 1, 4, 2, 8, 6, 5]
print(quicksort(arr))