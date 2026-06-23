#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : progressive.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 21/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
def progressive(number, max_number):
    if number <= max_number:
        print(number)
        progressive(number + 1, max_number)

progressive(1, 10)