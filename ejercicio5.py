"""
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

from numpy import array


def sum(numeros:array):
    value = 0
    for n in numeros:
        value += n
    return value

def mult(numeros:array):
    value = 0
    for n in numeros:
        if value == 0:
            value = n
        value = value * n
    return value
