"""
En Python no existen punteros como en lenguajes como C o C++. En lugar de punteros, Python usa un sistema de referencias.

Explicación:

En Python, las variables no "apuntan" directamente a direcciones de memoria, sino que hacen referencia a los objetos. Cuando asignas una variable a otra, ambas variables se referencian al mismo objeto en memoria, en lugar de hacer una copia de ese objeto.

Esto se diferencia de lenguajes como C o C++, donde los punteros permiten manipular directamente la dirección de memoria de las variables. En Python, no puedes acceder a las direcciones de memoria ni realizar operaciones directas con ellas como podrías hacerlo con punteros.

"""

# Ejemplo:

a = [1, 2, 3]  # 'a' es una referencia a una lista
b = a  # 'b' también referencia la misma lista que 'a'

print(a)  # Muestra: [1, 2, 3]
print(b)  # Muestra: [1, 2, 3]

# Modificando a través de 'b'
b.append(4)

print(a)  # Muestra: [1, 2, 3, 4] (también cambia 'a' porque 'a' y 'b' referencian el mismo objeto)
print(b)  # Muestra: [1, 2, 3, 4]


### Explicación del código:


### Conclusión:

"""La unica diferencia visible es q no se usan punteros explícitos ni manipulación directa de direcciones de memoria. Esto hace que Python sea más seguro y fácil de usar, pero también significa que no puedes realizar las mismas operaciones de bajo nivel que puedes hacer en otros lenguajes como C o C++."""

#otra conclusion podria ser que no necesitas definir el tipo de dato, ya que lo hace internamente python

#tambien que python usa mas recursos para funcionar