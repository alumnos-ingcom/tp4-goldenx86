################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def minimo(lista):
    """Devuelve el menor valor de una lista dada"""
    valor = lista[0]
    for i in lista:
        if i < valor:
            valor = i
    return valor


def maximo(lista):
    """Devuelve el mayor valor de una lista dada"""
    valor = lista[0]
    for i in lista:
        if i > valor:
            valor = i
    return valor


if __name__ == "__main__":
    print(minimo([4, 3, 2, -50]))
    print(maximo([100, -585, 666, 86]))
