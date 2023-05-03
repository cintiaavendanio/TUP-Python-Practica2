"""Sum, Compresión de Listas, Map, Filter, Reduce."""

from typing import Iterable


def suma_cubo_pares_for(numeros: Iterable[int]) -> int:
    """Toma una lista de números, los eleva al cubo, y devuelve la suma de
    los elementos pares.

    Restricciones:
        - Utilizar dos bucles FOR.
        - No utilizar la función range.
        

    Referencias:
        - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions # noqa: E501
        - https://docs.python.org/3/library/functions.html#sum
    """
    listaDePares = []
    for i, elemento in enumerate(numeros):
        elemento = elemento ** 3
        if elemento % 2 == 0:
            listaDePares.append(elemento)
    for i, elemento in enumerate(listaDePares):
        suma = suma + elemento
    return suma

    # listaDeCubos=[]
    # for i, elemento in enumerate(numeros):
    #     elemento=elemento**3
    #     listaDeCubos.append(elemento)
    # for i, elemento in enumerate(listaDeCubos):
    #     if elemento%2==0:
    #         suma=elemento+suma
    # return suma



# NO MODIFICAR - INICIO
assert suma_cubo_pares_for([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################


def suma_cubo_pares_sum_list(numeros: Iterable[int]) -> int:
    """Re-Escribir utilizando comprension de listas (debe resolverse en 1
    línea) y la función built-in sum.

    Ejemplo de comprension:
        nombreDeLaNuevaLista = [elemento for elemento in otraLista if condicion]

    Referencias:
        - https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions # noqa: E501
        - https://docs.python.org/3/library/functions.html#sum
    """
    return sum([elemento for elemento in numeros if (elemento**3)%2==0])

# NO MODIFICAR - INICIO
assert suma_cubo_pares_sum_list([1, 2, 3, 4, 5, 6]) == 288
# NO MODIFICAR - FIN


###############################################################################


#numeros = [1, 2, 3, 4, 5, 6]


"""
Escribir una función lambda que eleve los elementos al cubo

Restricción: Utilizar List, map y lambda y la variable numeros
"""
#filtrado = filter(lambda x: x % 2 != 0, mi_lista)
#numeros_al_cubo=lambda x:x**3

"""
Escribir una función lambda que permita filtrar todos los elementos pares

Restricción: Utilizar List, filter, lambda y la variable numeros_al_cubo
"""

#numeros_al_cubo_pares = filter(lambda x: x % 2==0, numeros_al_cubo) # Completar


"""
Escribir una función Lambda que sume todos los elementos

Restricción: Utilizar reduce, lambda y la variable numeros_al_cubo_pares
"""

from functools import reduce  # noqa: E402
#(reduce(funcion, objeto iterable))
#suma_numeros_al_cubo_pares = reduce(sum(numeros_al_cubo_pares),numeros_al_cubo_pares)  # Completar


# NO MODIFICAR - INICIO
#assert numeros_al_cubo == [1, 8, 27, 64, 125, 216]
#assert numeros_al_cubo_pares == [8, 64, 216]
#assert suma_numeros_al_cubo_pares == 288
# NO MODIFICAR - FIN
