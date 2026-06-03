#!/usr/bin/env python 
# -----------------------------------------------------
# Program    : selection_sort.py
# Description:
# Version    : 0.1
# Author     : Luca Gorayeb <lucagorayeb@gmail.com>
# Date       : 02/06/2026
# Lincence   : GNU/GPL v3.0
# -----------------------------------------------------
# Use:
# -----------------------------------------------------

def selection_sort(array):
    novo_array = []
    for i in range(len(array)):
        menor = encontra_menor(array)
        novo_array.append(array.pop(menor))
    return novo_array

def encontra_menor(array):
    menor = array[0]
    menor_indice = 0

    for i in range(len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

array = [20, 6, 5, 3, 2];
print(selection_sort(array))
