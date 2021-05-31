################
# Matías Locatti - @goldenx86
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


class IngresoIncorrecto(Exception):
    pass


def ingreso_entero_reintento(mensaje, cantidad_reintentos = 5):
    while cantidad_reintentos > 0:
        try:
            return int(input(mensaje + " #"))
        except ValueError as err:
            cantidad_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto(f"Falla al ingresar entero.")


def ingreso_entero_restringido(mensaje, valor_minimo = 0, valor_maximo = 10):
    valor = ingreso_entero_reintento(mensaje)
    if (valor < valor_minimo or valor > valor_maximo):
        raise IngresoIncorrecto("Valor fuera de rango.")
    return valor


if __name__ == "__main__":

    ingreso_entero_restringido("Ingrese un número entero: ")
