import random

# Elegimos una operación al azar entre las siguientes opciones
operaciones = ['+', '-', '*', '/', '**']
op = random.choice(operaciones)

# Si la operación es potencia, limitamos b a 4 para que no devuelva números muy grandes
a = random.randint(1, 10)
b = random.randint(1, 10 if op != '**' else 4)

# Ahora usamos if/elif para decidir qué operación hacer
if op == '+':
    resultado = a + b
elif op == '-':
    resultado = a - b
elif op == '*':
    resultado = a * b
elif op == '/':
    resultado = a / b if b != 0 else 'Error: división por cero'
elif op == '**':
    resultado = a ** b

# Mostramos el resultado
print(f"Operación generada: {a} {op} {b} = {resultado}")
