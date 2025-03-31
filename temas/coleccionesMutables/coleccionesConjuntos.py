
"""Esta clase ConjuntosEjemplos utiliza un método estático para demostrar diversas operaciones con conjuntos en Python, como agregar, eliminar, unir, intersectar y obtener diferencias. Los conjuntos en Python son útiles para almacenar colecciones de elementos únicos y realizar operaciones matemáticas de conjuntos de manera eficiente."""

class ConjuntosEjemplos:
    @staticmethod
    def ejemplos_conjuntos():
        print("--- Ejemplos con conjuntos ---")
        
        # Creación de un conjunto
        conjunto_a = {1, 2, 3, 4, 5}
        print("Conjunto inicial:", conjunto_a)  # {1, 2, 3, 4, 5}
        
        # Agregar un elemento
        conjunto_a.add(6)
        print("Después de add(6):", conjunto_a)  # {1, 2, 3, 4, 5, 6}
        
        # Eliminar un elemento con remove (genera error si no existe)
        conjunto_a.remove(3)
        print("Después de remove(3):", conjunto_a)  # {1, 2, 4, 5, 6}
        
        # Eliminar un elemento con discard (no genera error si no existe)
        conjunto_a.discard(10)
        print("Después de discard(10) (no afecta si no existe):", conjunto_a)
        
        # Unión de conjuntos
        conjunto_b = {4, 5, 6, 7, 8}
        print("Conjunto B:", conjunto_b)
        union = conjunto_a | conjunto_b
        print("Unión de A y B:", union)  # {1, 2, 4, 5, 6, 7, 8} #solo unio los valores unicos(sin repetidos)
        
        # Intersección de conjuntos
        interseccion = conjunto_a & conjunto_b
        print("Intersección de A y B:", interseccion)  # {4, 5, 6}
        
        # Diferencia de conjuntos
        diferencia = conjunto_a - conjunto_b
        print("Diferencia de A - B:", diferencia)  # {1, 2}
        
        # Diferencia simétrica (elementos únicos en cada conjunto)
        diferencia_simetrica = conjunto_a ^ conjunto_b
        print("Diferencia simétrica de A y B:", diferencia_simetrica)  # {1, 2, 7, 8}
        
        # Conversión de lista a conjunto para eliminar duplicados
        lista = [1, 2, 2, 3, 4, 4, 5]
        conjunto_desde_lista = set(lista) #set agarra una lista y la transforma en conjunto, por ende si tiene repetidos, los elimina.
        print("Lista original:", lista)
        print("Lista convertida en conjunto (sin duplicados):", conjunto_desde_lista)

# Ejecutar ejemplos
ConjuntosEjemplos.ejemplos_conjuntos()
