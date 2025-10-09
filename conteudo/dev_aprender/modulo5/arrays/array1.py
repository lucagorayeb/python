# Arrays 
from array import array

# Inteiros, números decimais e caracteres
numeros = array('i',[1,2,3,4,5,6])
print(numeros)
numeros.append(10)
print(numeros)
numeros.insert(3,278)
print(numeros)
numeros.pop(1)
print(numeros)
numeros.remove(5)
print(numeros)
del numeros[1]
print(numeros)

""" 
Código de tipo Tipo em C Tipo em Python Tamanho mínimo em

bytes

Notas

'b' signed char int 1
'B' unsigned char int 1
'u' Py_UNICODE Caractere unicode 2 -1
'h' signed short int 2
'H' unsigned short int 2
'i' signed int int 2
'I' unsigned int int 2
'l' signed long int 4
'L' unsigned long int 4
'q' signed long long int 8
'Q' unsigned long long int 8
'f' float float 4
'd' double float 8

"""