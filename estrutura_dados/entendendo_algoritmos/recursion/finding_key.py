#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : finding_key.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 21/06/2026
Lincence   : GNU/GPL v3.0
-----------------------------------------------------
Use: python3 finding_key.py
-----------------------------------------------------
"""
# Pseudo code. DO NOT EXECUTE.

# Function to finding a key using a while loop.
def finding_key(main_box):
    pile = main_box.create_pile_to_search()
    while pile is not None:
        box  = pile.take_box()
        for item in box:
            if item.is_box():
                pile.append()
            elif item.is_key():
                print("Key finded")

# Function to find a key using recursion 
def finding_key_recursive(main_box):
    for item in main_box:
        if item.is_box():
            finding_key_recursive(item)
        elif item.is_key():
            print("Key finded.")


print("It is a pseudo code.")
print("Do not execute!")