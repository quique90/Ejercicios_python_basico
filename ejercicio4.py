"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False
"""

def get_char(a):
    vocales = ['a','e','i','o','u']
    if a in vocales:
        return True
    else:
        return False

