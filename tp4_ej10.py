################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def factores_primos(numero):
    """Devuelve todos los factores primos de un número"""
    i = 1
    while i <= numero:
        factor = 0
        if numero % i == 0:
            j = 1
            while j <= i:
                if i % j == 0:
                    factor = factor + 1
                j = j + 1
            if factor == 2:
                print(i)
        i = i + 1


if __name__ == "__main__":
    num = int(input("Ingrese el número: "))
    print("Los factores primos son: ")
    print(factores_primos(num))
