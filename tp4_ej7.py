################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def division_lenta(dividendo, divisor):
    """Devuelve cociente y resto al entregar un dividendo y un divisor"""
    resto = dividendo
    cociente = 0
    while resto >= dividendo:
        resto = resto - divisor
        cociente = cociente + 1
        print(f"El cociente es: {cociente}")
        print(f"El resto es: {resto}")


if __name__ == "__main__":
    numero1 = int(input("Ingrese el dividendo: "))
    numero2 = int(input("Ingrese el divisor: "))
    print(division_lenta(numero1, numero2))
