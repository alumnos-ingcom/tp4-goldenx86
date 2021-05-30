################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ordenar_menor_a_mayor(uno, dos, tres):
    """Ordena de menor a mayor al ingresar 3 números"""
    lista = [uno, dos, tres]
    lista.sort()
    return tuple(lista)

def ordenar_mayor_a_menor(uno, dos, tres):
    """Ordena de mayor a menor al ingresar 3 números"""
    return ordenar_menor_a_mayor(uno, dos, tres)[::-1]


if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
    print(ordenar_menor_a_mayor(num1, num2, num3))
    print(ordenar_mayor_a_menor(num1, num2, num3))