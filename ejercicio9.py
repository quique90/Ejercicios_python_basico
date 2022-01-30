"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n:int, a:str):
    val = a
    for i in range(1,n):
        val += a
    return val

print(generar_n_caracteres(5,'x'))