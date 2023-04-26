"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union
"""Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.

    Restricciones:
        - Utilizar un bucle FOR.
        - Utilizar la función type.
        - No utilizar índices.
"""

def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    numeros = []
    strings = []
    for elemento in lista:
        #para contemplar que entren numeros
        # if type(elemento) == float or type(elemento) ==int:
        #     numeros.append(elemento)
        # else:
        #     strings.append(elemento)

        if type(elemento)==str:
            strings.append(elemento)
        else:
            numeros.append(elemento)
    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN


###############################################################################

"""Re-escribir utilizando comprensión de listas.

    Restricciones:
        - No utilizar bucles.
        - Utilizar dos comprensiones de listas.
"""
def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    #[expresion for variable in colección if condición]
    #"para cada variable de la colleccion si cumple con la condicion inserto ese elemento en la nueva lista"
    numeros = [elemento for elemento in lista if type(elemento) == int]
    strings = [elemento for elemento in lista if type(elemento) == str]
    return strings + numeros


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
