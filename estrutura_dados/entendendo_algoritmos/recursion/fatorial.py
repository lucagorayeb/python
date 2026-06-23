#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : fatorial.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 21/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""

# How fatorial works?
# n! = n - 1 * n - 2 * ... n - n

# Basic Step: 
# n - n = 1

# Recursive Step:
#  n - n != 1

def fatorial(number):
    if number != 1:
        return number * fatorial(number - 1)
        #fat = number * fatorial(number - 1)
        #print(fat)
        #return fat
    elif number == 1:
        #print(number)
        return number

print(fatorial(15))