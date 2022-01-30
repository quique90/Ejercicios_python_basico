"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1, n2, n3):
    numeros = [n1, n2, n3]
    mayor = None
    for n in numeros:
        if mayor == None or n > mayor:
            mayor = n
    return mayor

print(max_de_tres(1,500,3))