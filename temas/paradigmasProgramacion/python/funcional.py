#El paradigma funcional evita efectos secundarios y se enfoca en el uso de funciones puras, inmutabilidad y la evaluación de las expresiones.

# Calculando la suma de los números del 1 al 5 de manera funcional
from functools import reduce

def calcular_suma():
    return reduce(lambda x, y: x + y, range(1, 6)) #funcionamiento al final

# Llamamos a la función
resultado = calcular_suma()
print(f"La suma es: {resultado}")


#que son las funciones puras?

"""En el contexto de la programación funcional, una función pura es una función que cumple dos propiedades fundamentales:

    La función no modifica ningún estado externo ni interactúa con el mundo exterior. No cambia variables globales, sin realizar operaciones de entrada/salida (como imprimir en pantalla, escribir o interactuar con bases de datos).

    Para los mismos parámetros de entrada siempre retorna el mismo resultado. No depende de ningún estado externo y su salida está completamente determinada por sus parámetros de entrada.

    Ejemplo de una funcion pura:

        def suma(a, b):
            return a + b

    Ejemplo de una funcion no pura:

        contador = 0

        def incrementar():
            global contador
            contador += 1
            return contador

    """

"""
    reduce(lambda x, y: x + y, range(1, 6)):
    
    a. range(1,6) generan los numeros 1,2,3,4 y 5
    b. reduce posiciona el 1 y el 2 y los suma -> 1+2=3
    c. toma el 3 y lo suma al resultado anterior -> 3+3 =6
    d. toma el resultado, es decir 6 y lo suma al siguiente valor generado por range, es decir el 4 -> 6+4 = 10
    e. por ultimo toma el 10 y lo suma al ult Nro generado por range el 5 y da 15
"""