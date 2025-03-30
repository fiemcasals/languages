#Paradigma Imperativo

#En el paradigma imperativo, el foco está en cómo hacer las cosas, es decir, en una secuencia de instrucciones para el estado del programa.

# Calculando la suma de los números del 1 al 5 de manera imperativa

suma = 0
for i in range(1, 6):
    suma += i  # Modificar el estado de 'suma' en cada iteración
    
print(f"La suma es: {suma}")
