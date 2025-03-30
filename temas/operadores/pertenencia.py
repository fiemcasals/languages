"""Operadores de Pertenencia

Se utilizan para verificar si un valor pertenece a una secuencia, como una lista o un string."""


lista = [1, 2, 3, 4, 5]
cadena = "Hola Mundo"

# in
print(3 in lista)  # Salida: True
print("Mundo" in cadena)  # Salida: True

# not in
print(10 not in lista)  # Salida: True
print("mundo" not in cadena)  # Salida: True
