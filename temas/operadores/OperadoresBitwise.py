"""Operadores Bitwise (A nivel de bits)

Estos operadores trabajan a nivel de bits de los números enteros."""

a = 5      # 0101 en binario
b = 3      # 0011 en binario

# AND a nivel de bits
print(a & b)  # Salida: 1 (0001 en binario)

# OR a nivel de bits
print(a | b)  # Salida: 7 (0111 en binario)

# XOR a nivel de bits
print(a ^ b)  # Salida: 6 (0110 en binario)

# NOT a nivel de bits
print(~a)     # Salida: -6 (complemento a dos) ->es el negativo del numero siguiente. Al final dejo la explicacion real

# Desplazamiento a la izquierda (a = 5 = 0101)
print(a << 1)  # Salida: 10 (1010 en binario)
#equivale a multiplicar por dos la cantidad de veces que especifique. Partiendo siempre del resultado anterior.
#ej: (a<<3): Siendo a = 5:
#                5*2=10
#                10*2=20
#                20*2=40

print("demostracion exponencial")
print(a<<3) #va a dar 40


# Desplazamiento a la derecha

print(a >> 1)  # Salida: 2 (0010 en binario) #equivale a div por 2 con redondeo hacia abajo
#General: a >> n equivale a dividir a por 2^n

c=40

#ej: (c>>3): Siendo c = 40:
#                40/2=20
#                20/2=10
#                10*2=5

print(c>>3)  #deberia dar 5



"""El operador `~` en Python es el **complemento a dos** a nivel de bits. Este operador toma el valor binario de un número y lo invierte, cambiando todos los bits de 0 a 1 y de 1 a 0.

Para entenderlo mejor, aquí te explico el proceso paso a paso:

Ejemplo:

Supongamos que tienes el siguiente código:

                                                a = 5
                                                print(~a)


Paso 1: Representación binaria del número
En Python, los números enteros se representan en complemento a dos en binario. Primero, representemos `a = 5` en binario usando 8 bits para simplicidad:

5 en binario: 00000101

Paso 2: Aplicar el operador `~`
El operador `~` invierte todos los bits de la representación binaria:

~00000101  ->  11111010


Paso 3: Interpretación en complemento a dos
Ahora, la representación binaria `11111010` está en complemento a dos. Para obtener el valor decimal, debemos hacer lo siguiente:

1. Invertimos los bits: `00000101`.
2. Sumamos 1: `00000101 + 1 = 00000110`, lo que da `6`.
3. Como estamos trabajando en complemento a dos, el resultado es negativo, por lo que el valor final es `-6`.

Resultado final
Cuando imprimes el valor de `~5`, el resultado es `-6`, que es el complemento a dos de 5.

Resumen
El operador `~` invierte los bits de un número en su representación binaria, y en el contexto de los números enteros con complemento a dos, este operador produce el negativo del valor original menos uno. 

Así que: ~5 = -6
"""