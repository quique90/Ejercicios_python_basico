"""
Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(a):
    r = a[::-1]
    if r == a:
        return True
    else:
        return False
