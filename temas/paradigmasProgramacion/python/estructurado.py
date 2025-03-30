
#El paradigma estructurado es una forma del paradigma imperativo donde sigue una estructura clara utilizando funciones, condiciones y bucles para organizar el código.

# Calculando la suma de los números del 1 al 5 de manera estructurada
def calcular_suma():
    suma = 0
    for i in range(1, 6):
        suma += i
    return suma

def mostrar_resultado():
    resultado = calcular_suma()  # Llamamos a la función calcular_suma
    print(f"La suma es: {resultado}")

# Llamamos a la función principal que organiza todo
mostrar_resultado()
