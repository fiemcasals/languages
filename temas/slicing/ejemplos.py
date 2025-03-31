class SlicingExamples:
    def __init__(self, data):
        """Inicializa la clase con una secuencia (cadena, lista, etc.)."""
        self.data = data
    
    def get_slice(self, start=None, end=None, step=None):
        """Devuelve un subconjunto de la secuencia usando slicing."""
        return self.data[start:end:step]
    
    def reverse(self):
        """Devuelve la secuencia invertida usando slicing."""
        return self.data[::-1]
    
    def copy(self):
        """Devuelve una copia de la secuencia."""
        return self.data[:]
    
# Ejemplos con cadenas
texto = "Hola que tal"
texto_slicing = SlicingExamples(texto)
print("Texto original:", texto)
print("Subcadena [3:10]:", texto_slicing.get_slice(3, 10))
print("Desde el índice 4 hasta el final:", texto_slicing.get_slice(4))
print("Desde el inicio hasta el índice 10:", texto_slicing.get_slice(None, 10))
print("Copia del texto:", texto_slicing.copy())
print("Texto invertido:", texto_slicing.reverse())

# Ejemplos con listas
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numeros_slicing = SlicingExamples(numeros)
print("\nLista original:", numeros)
print("Elementos del índice 2 al 7:", numeros_slicing.get_slice(2, 7))
print("Cada dos elementos:", numeros_slicing.get_slice(0, None, 2))
print("Lista invertida:", numeros_slicing.reverse())


