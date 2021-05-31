################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(number1, number2):
    """Compara 2 números y retorna -1 en caso del primero ser menor, 0 si"""
    """son iguales y 1 si el primero es mayor"""
    if number1 < number2:
        return -1
    elif number1 > number2:
        return 1
    else:
        return 0

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(compara(num1,num2))
