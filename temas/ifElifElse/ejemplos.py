# Estructuras de control if/elif/else, se utilizan para evaluar un condicional, es decir, si cumple tal condicion, hace tal cosa, sino y cumple tal otra condicion hace tal otra cosa, y si no cumple nada de lo anterior, ejecuta tal instruccion"

def calcular_impuesto(ingresos):
    """Calcula el impuesto basado en los ingresos usando if/elif/else."""
    coeficiente = 0.05  # Valor por defecto
    
    if ingresos < 30000:
        coeficiente = 0.1
    elif ingresos < 66000:
        coeficiente = 0.15
    else:
        coeficiente = 0.35
    
    return ingresos * coeficiente

# Ejemplo de uso
ingresos = float(input("Ingrese sus ingresos anuales: ")) #float convierte la entrada en un número decimal
impuesto = calcular_impuesto(ingresos)
print("Resultado impuestos:", impuesto)

# Ejemplo adicional con múltiples condiciones
def clasificar_edad(edad):
    """Clasifica a una persona según su edad."""
    if edad < 12:
        return "Niño"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"

# Uso de la función
edad = int(input("Ingrese su edad: "))
clasificacion = clasificar_edad(edad)
print("Clasificación por edad:", clasificacion)

# Importancia de la indentación en Python
def ejemplo_indentacion():
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("Es cero")

# Ejecutar ejemplo de indentación
ejemplo_indentacion()


# Ejemplo con operador ternario
ingresos = float(input("Ingrese sus ingresos anuales: "))  # Convertimos la entrada en número decimal

# Uso del operador ternario
coeficiente = 0.1 if ingresos < 30000 else 0.15
print("Resultado impuestos:", ingresos * coeficiente)

# Uso de la notación alternativa con tupla
coeficiente = (0.15, 0.1)[ingresos < 30000] #el orden -> v,f
print("Resultado impuestos (método alternativo):", ingresos * coeficiente)

# Otro ejemplo: Determinar si un número es par o impar usando el operador ternario
numero = int(input("Ingrese un número: "))  # Convertimos la entrada de str a un número entero
tipo = "Par" if numero % 2 == 0 else "Impar"
print("El número ingresado es:", tipo)
