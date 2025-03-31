
# Convertir un número decimal a binario usando while

n = 57845
restos = []

# Mientras el número sea mayor que 0, continuamos dividiéndolo entre 2
while n > 0:
    remainder = n % 2  # Calculamos el residuo de la división entre 2
    restos.append(remainder)  # Almacenamos el residuo en la lista
    n //= 2  # Realizamos la división entera entre 2

# Al final, los restos contienen los bits, pero están en orden inverso
restos.reverse()  # Invertimos la lista para tener la representación binaria correcta

print(restos)  # Imprimimos la representación binaria #[1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]

"""Explicación del Código
1. Inicialización:  
   Se empieza con un número 'n = 57845' y una lista vacía 'restos = []' donde se almacenarán los restos de las divisiones sucesivas.

2. Condición while:  
   El ciclo sigue ejecutándose mientras 'n' sea mayor que '0'. En cada iteración, calculamos el residuo ('remainder') de la división de 'n' entre '2', lo que nos da el bit de la representación binaria. Luego, agregamos este bit a la lista 'restos'.

3. División:  
   Después de calcular el residuo, realizamos una división entera ('n //= 2') para reducir el valor de 'n' y proceder con la siguiente iteración. #// div entera

4. Invertir la lista:  
   Al finalizar el ciclo, los restos estarán en orden inverso, por lo que usamos 'restos.reverse()' para invertir la lista y obtener la representación binaria correcta.

¿Por qué usar 'while' aquí? 
El ciclo 'while' es adecuado en este caso porque no sabemos cuántas veces necesitaremos dividir el número 'n' hasta llegar a '0'. El ciclo se ejecutará hasta que 'n' sea igual a '0', lo cual es la condición de paro natural de este proceso de conversión."""