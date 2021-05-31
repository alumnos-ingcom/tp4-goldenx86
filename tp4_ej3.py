################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit(celsius):
    """Convertir a unidades de países especiales"""
    retarded = (celsius * (9/5)) + 32
    return retarded

def convertir_a_centigrados(retarded):
    """Convertir a unidades con lógica y sentido"""
    celsius = (retarded -32) * (5/9)
    return celsius

if __name__ == "__main__":
    temp = int(input("Ingrese la temperatura a convertir en unidades especiales: "))
    print(convertir_a_fahrrenheit(temp))
    temp = int(input("Ingrese la temperatura a convertir en grados celsius: "))
    print(convertir_a_centigrados(temp))
