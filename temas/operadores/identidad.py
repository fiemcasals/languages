"""Operadores de Identidad

Se utilizan para verificar si dos objetos son el mismo (mismo lugar en memoria)."""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# is (compara si son el mismo objeto en memoria)
print(a is b)  # Salida: True (b es el mismo objeto que a)

# is not (compara si no son el mismo objeto en memoria)
print(a is not c)  # Salida: True (a y c son diferentes objetos en memoria)
