import random

# random.random(): número decimal entre 0.0 y 1.0
print("\nvamos a imprimir un numero random entre 0.0 y 1.0 con random.random")
print("random():", random.random())

print("\nrandom.randint(a, b): número entero entre a y b, incluyendo ambos")
print("randint(1, 10):", random.randint(1, 10))

print("\nrandom.choice(lista): elige 1 elemento al azar de la lista")
print("choice(['sol', 'luna', 'estrella']):", random.choice(['sol', 'luna', 'estrella']))

print("\nrandom.choices(lista, k=n): elige n elementos al azar, puede repetir")
print("choices([1, 2, 3], k=5):", random.choices([1, 2, 3], k=5))

print("\nrandom.sample(lista, k=n): elige n elementos al azar, sin repetir")
print("sample([1, 2, 3, 4, 5], k=3):", random.sample([1, 2, 3, 4, 5], k=3))

print("\nrandom.shuffle(lista): mezcla una lista (modifica la lista original)")
cartas = ['A', 'K', 'Q', 'J']
random.shuffle(cartas)
print("shuffle(['A', 'K', 'Q', 'J']):", cartas)

print("\nrandom.uniform(a, b): número decimal entre a y b")
print("uniform(1.5, 3.5):", random.uniform(1.5, 3.5))

# -------------------------------------------
# random.seed(x): fija una "semilla" para que el resultado sea siempre igual
# Muy útil para depuración o reproducir resultados
random.seed(42)
print("\nSemilla fija con seed(42):")
print("random():", random.random())     # Siempre va a dar el mismo resultado
print("randint(1, 10):", random.randint(1, 10))  # También va a ser el mismo

# Si volvés a poner la misma semilla, obtendrás exactamente los mismos valores
random.seed(35)
print("\nRepetimos seed(35):")
print("random():", random.random())     # Mismo que antes
print("randint(1, 10):", random.randint(1, 10))  # Mismo que antes
