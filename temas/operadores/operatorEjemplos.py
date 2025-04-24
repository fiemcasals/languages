import operator  # Importamos todo el módulo operator

# Declaramos dos números para usar en las operaciones
a = 10
b = 3

# Suma → operator.add(a, b) es igual que a + b
resultado_suma = operator.add(a, b)
print("Suma (operator.add):", resultado_suma)  # 10 + 3 = 13

# Resta → operator.sub(a, b) es igual que a - b
resultado_resta = operator.sub(a, b)
print("Resta (operator.sub):", resultado_resta)  # 10 - 3 = 7

# Multiplicación → operator.mul(a, b) es igual que a * b
resultado_multiplicacion = operator.mul(a, b)
print("Multiplicación (operator.mul):", resultado_multiplicacion)  # 10 * 3 = 30

# División real → operator.truediv(a, b) es igual que a / b
resultado_division = operator.truediv(a, b)
print("División real (operator.truediv):", resultado_division)  # 10 / 3 = 3.333...

# División entera → operator.floordiv(a, b) es igual que a // b
resultado_division_entera = operator.floordiv(a, b)
print("División entera (operator.floordiv):", resultado_division_entera)  # 10 // 3 = 3

# Potencia → operator.pow(a, b) es igual que a ** b
resultado_potencia = operator.pow(a, b)
print("Potencia (operator.pow):", resultado_potencia)  # 10 ** 3 = 1000



"""@fiemcasals ➜ /workspaces/languages (insertarOrdenado) $ /home/codespace/.python/current/bin/python3 /workspaces/languages/temas/operadores/operator.py
Traceback (most recent call last):
  File "/workspaces/languages/temas/operadores/operator.py", line 1, in <module>
    import operator  # Importamos todo el módulo operator
    ^^^^^^^^^^^^^^^
  File "/workspaces/languages/temas/operadores/operator.py", line 8, in <module>
    resultado_suma = operator.add(a, b)
                     ^^^^^^^^^^^^
AttributeError: partially initialized module 'operator' has no attribute 'add' (most likely due to a circular import)"""