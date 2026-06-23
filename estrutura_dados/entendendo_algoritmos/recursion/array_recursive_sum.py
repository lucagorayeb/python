#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : array_recursive_sum.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 21/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
def array_recursive_sum(array):
    if len(array) != 0:
        return array.pop() + array_recursive_sum(array)
    else:
        return 0

print(array_recursive_sum([4, 5, 6, 1]))