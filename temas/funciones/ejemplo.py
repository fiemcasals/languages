# funciones_basicas.py
# Clase práctica: Introducción a funciones en Python

# 🔹 Función sin parámetros
def saludar():
    print("¡Hola! Bienvenido a la clase de funciones.")

# 🔹 Función con un parámetro
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}! ¿Cómo estás?")

# 🔹 Función con dos parámetros, sin retorno
def sumar(a, b):
    resultado = a + b
    print(f"La suma de {a} + {b} es: {resultado}")

# 🔹 Función con dos parámetros y con retorno
def multiplicar(x, y):
    return x * y

# 🔹 Función sin parámetros, solo muestra un menú
def mostrar_menu():
    print("\n📋 MENÚ PRINCIPAL")
    print("1. Saludar")
    print("2. Calcular área de un triángulo")
    print("3. Salir")

# 🔹 Función con parámetro: ejecuta según opción elegida
def opcion_seleccionada(opcion):
    if opcion == 1:
        nombre = input("Ingresá tu nombre: ")
        saludar_persona(nombre)
    elif opcion == 2:
        base = float(input("Ingresá la base: "))
        altura = float(input("Ingresá la altura: "))
        area = calcular_area(base, altura)
        print(f"El área del triángulo es: {area}")
    elif opcion == 3:
        print("👋 ¡Gracias por participar!")
    else:
        print("⚠️ Opción inválida.")

# 🔹 Función que calcula el área de un triángulo y devuelve el valor
def calcular_area(base, altura):
    return (base * altura) / 2

# 🔸 Pruebas simples de las funciones
saludar()
saludar_persona("Lucía")
sumar(5, 10)
print("Multiplicación con return:", multiplicar(4, 6))

# 🔸 Menú interactivo
while True:
    mostrar_menu()
    try:
        seleccion = int(input("Seleccioná una opción: "))
        opcion_seleccionada(seleccion)
        if seleccion == 3:
            break
    except ValueError:
        print("⚠️ Por favor ingresá un número válido.")
