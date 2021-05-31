################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_primo(numero):
    """Revisa si un número es primo"""
    if numero > 1:
        for i in range(2, int(numero/2) + 1):
            if numero % i != 0:
                primo = True
            else:
                primo = False
    else:
        primo = False

    if numero < -1:
        numero = (numero * -1)
        for i in range(2, int(numero / 2) + 1):
            if numero % i != 0:
                primo = True
            else:
                primo = False
    else:
        primo = False

    if primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

if __name__ == "__main__":
    num = int(input("Ingrese el número: "))
    print(es_primo(num))
