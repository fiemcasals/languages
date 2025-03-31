
for i in range(0,10,1):
    print("hola")



#numeros aleatorios

import random

for i in range(10):  # Genera 10 números aleatorios
    print(random.randint(1, 100))  # Número aleatorio entre 1 y 100


#ciudades  y nombres de un conjunto

import random

nombres = ["Carlos", "Ana", "Luis", "Sofía", "Pedro", "María"]
ciudades = ["Madrid", "Buenos Aires", "Ciudad de México", "Lima", "Bogotá", "Santiago"]

for i in range(10):  # Genera 10 combinaciones aleatorias
    nombre = random.choice(nombres)
    ciudad = random.choice(ciudades)
    print(f"{nombre} - {ciudad}")


#nombres falsos y ciudades falsas
#primero debo instalar: pip install faker


from faker import Faker

fake = Faker()

for i in range(10):  # Genera 10 combinaciones aleatorias
    nombre = fake.name()
    ciudad = fake.city()
    print(f"{nombre} - {ciudad}")
