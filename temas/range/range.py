class RangosEjemplos:
    """Clase que demuestra el uso de la función range en Python."""

    @staticmethod #no recibe self, ni cls
    def crear_rango(inicio, fin, paso):
        """Crea un rango con los parámetros dados y lo convierte en una lista."""
        return list(range(inicio, fin, paso))
    

    @staticmethod
    def obtener_elemento(rango_lista, indice):
        """Obtiene un elemento específico de la lista generada por range."""
        return rango_lista[indice]

    @staticmethod
    def obtener_sublista(rango_lista, inicio, fin):
        """Obtiene una sublista desde la lista generada por range."""
        return rango_lista[inicio:fin]
    #toma el indice, ej: inicio == 3 imprime el cuarto numero del vector y ya que el primer numero es el indice 0

    @staticmethod
    def imprimir_rango(rango_lista):
        """Imprime los elementos de la lista generada por range."""
        print(", ".join(map(str, rango_lista))) #str lo que hace es convertir los numeros en str para poder aplicar el metodo join. mientras que map aplica el str a cada elemento de la lista

    
# Uso de la clase RangosEjemplos

# Crear un rango de 1 a 100 con incrementos de 2
a = RangosEjemplos.crear_rango(1, 100, 2)
print(a) #imprime directamente la lista
print("Lista generada por range(1, 100, 2):")
RangosEjemplos.imprimir_rango(a)

# Crear un rango de 0 al -100 con incrementos de 2
a = RangosEjemplos.crear_rango(0, -100, -2)
print(a) #imprime directamente la lista
print("Lista generada por range(0, -100, -2):")
RangosEjemplos.imprimir_rango(a)

# Convertir el rango en una lista
b = list(a)
print("\nLista convertida:", b)

# Obtener una sublista
sublista = RangosEjemplos.obtener_sublista(b, 5, 10)
print("\nSublista b[5:10]:", sublista)

# Obtener el último elemento (equivalente a acceder al último índice en C)
ultimo_elemento = RangosEjemplos.obtener_elemento(b, -1)
print("\nÚltimo elemento de b (-1):", ultimo_elemento)


