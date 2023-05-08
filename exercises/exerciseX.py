from typing import List, Union

###############################################################################


def maximo_recursivo(*args) -> float:
    max = args[0]
    for elemento in args:
        if max < elemento:
            max = elemento
    return max
    # return reduce(lambda x,y: x if x>y else y, args)

    """Toma una cantidad arbitraria de números y devuelve el mayor.

    Restricciónes:
        - No utilizar la función max
        - No utilizar la ninguna otra función salvo maximo_recursivo
        - Resolver de manera recursiva
    """


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert maximo_recursivo(1, 10, 5, -5) == 10
    assert maximo_recursivo(4, 9, 18, 6) == 18
    assert maximo_recursivo(24, 9, 18, 20) == 24
    assert maximo_recursivo(24, 9, 18, 30) == 30
# NO MODIFICAR - FIN


###############################################################################


from functools import reduce  # noqa: E402


def sumatoria_reduce(n: int) -> int:
    return reduce(lambda x,y: x+y, range(n+1))

    """Devuelve la suma de los números de 1 a N.

    Restricción: Utilizar la función reduce.
    Referencia: https://docs.python.org/3/library/functools.html#functools.reduce  # noqa: E501
    """


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:  # noqa: E501
    return sorted(lista, key=lambda item: type(item) is int)
    """Re-escribir utilizando la función sorted con una custom key.

    Restricciones:
        - No utilizar bucles.
        - No utilizar comprensiones.
        - Utilizar un lambda.

    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]  # noqa: E501
# NO MODIFICAR - FIN
