#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : try_catch.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 15/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
""" try:
    arquivo = open("teste_try_except.txt", "r")
    conteudo = arquivo.read()
#except FileNotFoundError:
#    print("Arquivo não encontrado.")
except Exception as error:
    print(f"Erro inesperado: {error}")
finally:
    print("Bloco finaly executado.") """

try:
    print("Olá mundo!")
except Exception as error:
    print(f"Erro inesperado: {error}")


