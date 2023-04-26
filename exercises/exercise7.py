"""Any y Sets."""

from typing import Any, Iterable

"""Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricciones:
        - Utilizar dos bucles FOR anidados.
        - Utilizar dos returns.

        lista_1=(1,2,3,4)
        lista_2=(2,7,8)
"""
def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:  # noqa: E501
    for elemento1 in lista_1:
            for elemento2 in lista_2:
                if elemento1 == elemento2:
                    return True
            
    return False
            

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################

"""Re-Escribir utilizando un sólo bucle y el operador IN.

    Restricciones:
        - Utilizar un único bucle FOR.
        - Utilizar dos returns.
    """
def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
   for elemento in lista_1:
     if elemento in lista_2:
         return True
         


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando la funcion any.

    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea.

    Referencia: https://docs.python.org/3/library/functions.html#any

    [elemento for elemento in lista if type(elemento) == int]
    """

def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    #creamos una lista con elementos que tienen en comun
    #si una lista es vacia--> devuelve False
    return any([elemento for elemento in lista_1 if elemento in lista_2])
    #de otra forma:
    #return any(elemento in lista_2 for elemento in lista_1)

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################
"""Re-Escribir utilizando conjuntos (sets).

    Restricciones:
        - Resolver sólo utilizando operaciones de conjuntos
        - No utilizar ANY, ALL, FOR, IF ni COMPRENSIONES

    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset  # noqa: E501
    """

def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    #la funcion set convierte cada lista en un conjunto, aplicando esto podemos utilizar las operaciones de conjuntos (union, interseccion,etc)
    return set(lista_1)&set(lista_2)
    #de otra forma:
    #return set(lista_1).intersection(set(lista_2))


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
