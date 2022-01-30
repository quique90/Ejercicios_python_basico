"""
Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.)
"""

def get_len(a):
    return a.__len__()

print(get_len('hola'))