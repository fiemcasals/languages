# ------------------------------------------
# 🔁 FOR más básico: recorre letras de una palabra
# ------------------------------------------
for letra in "hola":
    print(letra)

# ------------------------------------------
# 🔁 FOR anidado básico: letras de varias palabras
# ------------------------------------------
palabras = ["hola", "chau"]

for palabra in palabras:
    print("Palabra:", palabra)
    for letra in palabra:
        print(" Letra:", letra)

# ------------------------------------------
# 🔁 FOR básico con números usando range()
# ------------------------------------------
for numero in range(1, 6):
    print(numero)

# ------------------------------------------
# 🔁 FOR anidado: tablas de multiplicar del 1 al 3
# ------------------------------------------
for i in range(1, 4):
    print("Tabla del", i)
    for j in range(1, 4):
        print(f" {i} x {j} = {i * j}")

# ------------------------------------------
# 🔁 FOR simple recorriendo una lista
# ------------------------------------------
numeros = [1, 2, 3, 4, 5]

print("\nimprime los cinco numeros de la lista")
for numero in numeros:
    print(numero)

# ------------------------------------------
# 🔁 FOR anidado con listas dentro de listas (matriz)
# ------------------------------------------
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print("\n")
for fila in matriz:
    for elemento in fila:
        print(elemento)
    print("\n")
