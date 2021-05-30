################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def palindromo(texto):
    """Revisa si un texto es un palíndromo"""
    if texto == texto[::-1]:
        print("El texto es un palíndromo.")
    else:
        print("El texto no es un palíndromo.")


if __name__ == "__main__":
    text = str(input("Ingrese el texto a verificar: "))
    print(palindromo(text))