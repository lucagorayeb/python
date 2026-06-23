#!/usr/bin/env python 
# -----------------------------------------------------
# Program    : assimetria_data_objeto.py
# Description:
# Version    : 0.1
# Author     : Luca Gorayeb <lucagorayeb@gmail.com>
# Date       : 04/06/2026
# Lincence   : GNU/GPL v3.0
# -----------------------------------------------------
# Use:
# -----------------------------------------------------
from abc import ABC, abstractmethod

class Area(ABC):

    @abstractmethod
    def calcularArea(self):
        pass

class Quadrado(Area):
    def calcularArea(self, lado):
        return lado * lado

class Retangulo(Area):
    def calcularArea(self, base, altura):
        return base * altura

q = Quadrado()
print(q.calcularArea(10))

r = Retangulo()
print(r.calcularArea(10, 3))
