"""Paradigma Lógico

El paradigma lógico está basado en hechos y reglas. Aunque Python no es un lenguaje lógico de puro, se puede simular el comportamiento lógico de las bibliotecas como kanren."""

from kanren import run, var, Relation, facts

# Definir una relación "progenitor"
progenitor = Relation()

# Definir hechos (Juan es progenitor de Maria y Pedro)
facts(progenitor, ("juan", "maria"), ("juan", "pedro"))

# Realizar la consulta (¿Quiénes son los progenitores de Juan?)
X = var()

resultado = run(1, X, progenitor("juan", X))  # Buscar a los progenitores de Juan, 1 para unica solucion, x buscamos el valor de x para la cual es verdadero que juan es progenitor de esa x

print(f"Progenitores de Juan: {resultado}") #Progenitores de Juan: ('maria',), si quisiera saber de pedro tambien, tendria que poner 2 en vez de 1. "resultado = run(2, X, progenitor("juan", X))  # Buscar hasta 2 progenitores de Juan"
