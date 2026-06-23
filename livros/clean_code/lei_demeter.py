#!/usr/bin/env python 
# -----------------------------------------------------
# Program    : lei_demeter.py
# Description:
# Version    : 0.1
# Author     : Luca Gorayeb <lucagorayeb@gmail.com>
# Date       : 04/06/2026
# Lincence   : GNU/GPL v3.0
# -----------------------------------------------------
# Use:
# -----------------------------------------------------

from abc import ABC, abstractmethod

class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.__motor = Motor()

    def ligarMotor(self):
       self.__motor.ligar()

class Pessoa:
    def __init__(self):
        self.__carro = Carro()

    def ligarCarro(self):
        self.__carro.ligarMotor()

p = Pessoa()
p.ligarCarro()
