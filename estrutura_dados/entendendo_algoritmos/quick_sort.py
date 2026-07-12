#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : quick_sort.py
Description:
Version    : 0.1
Author     : Luca Gorayed <lucagorayeb@gmail.com>
Date       : 23/06/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
# Quicksort

# Global Variables:
# size
# pivo

# Basic Case:
# array size < 2 
#   return array[0]

# Recursive/Inductive Case:
# array size > 2
#   array[i] > pivo
#       add element to new array an
#   array[i] < pivo
#       add element to new array b
#
# array size == 2
#   array[0] > array[1]
# 
def quick_sort(number_list):
    size = len(number_list)
    if  size < 2:
        return number_list
    else:
        pivo = number_list[0]
        small = [i for i in number_list[1:] if i <= pivo]
        big = [i for i in number_list[1:] if i > pivo]
        return quick_sort(small) + [pivo] + quick_sort(big)

array = [10, 5, 2, 3]
r = quick_sort(array)
print(r)