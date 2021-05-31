################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero1,numero2):
    """Suma lenta de dos números positivos o negativos."""
    i = 0
    if numero1 > 0:
        while numero1 > 0:
            i = i + 1
            numero1 = numero1 - 1
    if numero2 > 0:
        while numero2 > 0:
            i = i + 1
            numero2 = numero2 - 1
    if numero1 < 0:
        while numero1 < 0:
            i = i - 1
            numero1 = numero1 + 1
    if numero2 < 0:
        while numero2 < 0:
            i = i - 1
            numero2 = numero2 + 1
    return i

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(suma_lenta(num1,num2))