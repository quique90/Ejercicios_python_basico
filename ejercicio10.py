"""
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******


"""

def procedimiento(numeros:list):
    for n in numeros:
        l = len(numeros)
        val = ''
        for i in range(0,n):
            val += '*'
        print(val)

procedimiento([4,9,7])