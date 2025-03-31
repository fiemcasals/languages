
# Usamos filter() para obtener números pares en un rango de 1000
pares = list(filter(lambda x: x % 2 == 0, range(1000)))
print(pares)

# Uso de break para detener el bucle en el número 500
for num in pares:
    if num > 500:
        break
    print(num, end=" ")

print("\n---")

# Uso de continue para omitir los múltiplos de 100
for num in pares[:60]:  # Solo los primeros 60 elementos #en este caso el unico numero q no imprime es el 100, ya que num % 100 son solo 100 200 300...y analiza los primero 60 numeros...
    if num % 100 == 0:
        continue
    print(num, end=" ")

print("\n---")

# Uso de map() para elevar al cuadrado los números pares hasta 20
pares_cuadrados = list(map(lambda x: x ** 2, pares[:10]))
print(pares_cuadrados)
