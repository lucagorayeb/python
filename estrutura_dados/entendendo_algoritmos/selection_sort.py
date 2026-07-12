#!/usr/bin/env python 
# -----------------------------------------------------
# Program    : selection_sort.py
# Description:
# Version    : 0.1
# Author     : Luca Gorayeb <lucagorayeb@gmail.com>
# Date       : 02/06/2026
# Licence   : GNU/GPL v3.0
# -----------------------------------------------------
# Use:
# -----------------------------------------------------
def selection_sort(number_list):
    new_array = []
    for i in range(len(number_list)):
        minor = find_minor(number_list)
        new_array.append(number_list.pop(minor))
    return new_array


def find_minor(selection_list):
    minor = selection_list[0]
    minor_number = 0

    for i in range(len(selection_list)):
        if selection_list[i] < minor:
            minor = selection_list[i]
            minor_number = i
    return minor_number


array = [20, 6, 5, 3, 2]
print(selection_sort(array))
