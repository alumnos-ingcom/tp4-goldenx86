################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convert_to_retarded_units(celsius):
    """Convertir a unidades de países especiales"""
    retarded = (celsius * (9/5)) + 32
    return retarded

def convert_to_celsius(retarded):
    """Convertir a unidades con lógica y sentido"""
    celsius = (retarded -32) * (5/9)
    return celsius

if __name__ == "__main__":
    temp = int(input("Ingrese la temperatura a convertir en unidades especiales: "))
    print(convert_to_retarded_units(temp))
    temp = int(input("Ingrese la temperatura a convertir en grados celsius: "))
    print(convert_to_celsius(temp))