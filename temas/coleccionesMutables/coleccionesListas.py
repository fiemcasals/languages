
"Una colección mutable es una estructura de datos que permite modificar su contenido después de su creación. Esto significa que se pueden agregar, eliminar o cambiar elementos dentro de la colección sin necesidad de crear una nueva instancia."


class ColeccionesEjemplos:
    """
    Clase que demuestra el uso de colecciones mutables en Python,
    sobrecarga de operadores y métodos de listas y bytearrays.
    """

    @staticmethod #no dependen de la instancia (self) ni de la clase (cls). -> no requiere de los datos internos
    def ejemplos_listas(): #al ser estaticmethod no recibe self, ya que no lo necesita
        print("--- Ejemplos con listas ---")
        
        # Creación de una lista
        a = list("Hola")
        print("Lista inicial:", a) #Lista inicial: ['H', 'o', 'l', 'a']
        
        # Agregar un elemento al final
        a.append("!")
        print("Después de append('!'):", a)#Después de append('!'): ['H', 'o', 'l', 'a', '!']
        
        # Insertar un elemento en un índice específico
        a.insert(3, "M")
        print("Después de insert(3, 'M'):", a) #Después de insert(3, 'M'): ['H', 'o', 'l', 'M', 'a', '!']
        
        # Eliminar el último elemento con pop
        eliminado = a.pop() #a.pop() == !
        print("Elemento eliminado con pop():", eliminado) #Elemento eliminado con pop(): !
        print("Lista después de pop():", a) #Lista después de pop(): ['H', 'o', 'l', 'M', 'a']
        
        # Ordenar una lista de números
        numeros = [3, 1, 4, 1, 5, 9, 2]
        print("Lista antes de ordenar:", numeros) #Lista antes de ordenar: [3, 1, 4, 1, 5, 9, 2]
        numeros.sort()
        print("Lista después de ordenar:", numeros) #Lista después de ordenar: [1, 1, 2, 3, 4, 5, 9]
        
    
    
   
# Ejecutar ejemplos
ColeccionesEjemplos.ejemplos_listas()
ColeccionesEjemplos.ejemplos_operator_overloading()

