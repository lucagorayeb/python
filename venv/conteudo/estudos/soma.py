def soma(arr):
    for i in range(3):
        if arr == []:
            return 0
        else:
            valor = arr[i] 
            arr.pop(0)
            return valor + soma(arr)

arr = [2,4,6,8]
print(soma(arr)) 

