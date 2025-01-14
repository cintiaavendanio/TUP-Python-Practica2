"""For, Sum, Reduce."""

"""Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar un bucle FOR.
"""
def sumatoria_basico(n: int) -> int:
    suma = 0
    for i in range(1, n+1):
        #desde el 1 hasta el segundo parametro sin incluir
        #suma=suma+i
        suma += i
    return suma


# NO MODIFICAR - INICIO
assert sumatoria_basico(1) == 1
assert sumatoria_basico(100) == 5050
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando la función sum.

    Restricción: No utilizar bucles (FOR, WHILE, etc)
    Referencia: https://docs.python.org/3/library/functions.html#sum
"""

def sumatoria_sum(n: int) -> int:
    numeros = range(1, n+1)
    return sum(numeros)
# utiliza la función range() para crear una secuencia de números del 1 al n.

# NO MODIFICAR - INICIO
assert sumatoria_sum(1) == 1
assert sumatoria_sum(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


from typing import Iterable  # noqa: E402

"""Toma un lista de números y devuelve el producto todos los números. Si
    la lista está vacia debe devolver 0.

    Restricciones:
        - No usar bibliotecas auxiliares (Numpy, math, pandas).
        - Utilizar un bucle FOR
        - Utilizar múltiples Return
        - No utilizar ELSE
"""
def multiplicar_basico(numeros: Iterable[float]) -> float:
    producto=1
    if numeros:
        for i in numeros:
           producto=producto*i
        return producto
    
    return 0
#si una lista tiene datos es true sino es false


# NO MODIFICAR - INICIO
assert multiplicar_basico([1, 2, 3, 4]) == 24
assert multiplicar_basico([2, 5]) == 10
assert multiplicar_basico([]) == 0
assert multiplicar_basico([1, 2, 3, 0, 4, 5]) == 0
# NO MODIFICAR - FIN
