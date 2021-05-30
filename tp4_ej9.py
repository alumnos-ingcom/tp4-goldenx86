################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def primo(numero):
    """Revisa si un número es primo"""
    if numero > 1:
        for i in range(2, int(numero/2) + 1):
            if numero % i != 0:
                es_primo = True
            else:
                es_primo = False
    else:
        es_primo = False

    if numero < -1:
        numero = (numero * -1)
        for i in range(2, int(numero / 2) + 1):
            if numero % i != 0:
                es_primo = True
            else:
                es_primo = False
    else:
        es_primo = False

    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

if __name__ == "__main__":
    num = int(input("Ingrese el número: "))
    print(primo(num))