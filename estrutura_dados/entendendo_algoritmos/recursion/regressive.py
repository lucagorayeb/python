#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : regressive.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 21/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
def regressive(number):
    if number > 0:
        print(number)
        regressive(number - 1)

regressive(10)