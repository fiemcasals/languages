""" 
Esta clase DiccionariosEjemplos utiliza un método estático para demostrar diversas operaciones con diccionarios en Python, como agregar, modificar, eliminar claves y valores, acceder a elementos, obtener claves, valores y elementos, fusionar diccionarios y recorrerlos.
Los diccionarios en Python son estructuras de datos clave-valor que permiten almacenar y acceder a los datos de manera eficiente.
"""

class DiccionariosEjemplos:
    @staticmethod
    def ejemplos_diccionarios():
        print("--- Ejemplos con diccionarios ---")

        # Creación de un diccionario
        diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
        print("Diccionario inicial:", diccionario) #Diccionario inicial: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

        # Acceder a un valor a través de su clave
        print("Nombre:", diccionario["nombre"])  # Nombre: Juan

        # Agregar una nueva clave-valor
        diccionario["profesion"] = "Ingeniero"
        print("Después de agregar 'profesion':", diccionario)#Después de agregar 'profesion': {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

        # Modificar un valor existente
        diccionario["edad"] = 31
        print("Después de modificar 'edad':", diccionario)#Después de modificar 'edad': {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

        # Eliminar una clave con del
        del diccionario["ciudad"]
        print("Después de eliminar 'ciudad':", diccionario)#Después de eliminar 'ciudad': {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero'}

        # Obtener todas las claves
        print("Claves del diccionario:", diccionario.keys())#Claves del diccionario: dict_keys(['nombre', 'edad', 'profesion'])

        # Obtener todos los valores
        print("Valores del diccionario:", diccionario.values())#Valores del diccionario: dict_values(['Juan', 31, 'Ingeniero'])

        # Obtener todos los pares clave-valor
        print("Elementos del diccionario:", diccionario.items())#Elementos del diccionario: dict_items([('nombre', 'Juan'), ('edad', 31), ('profesion', 'Ingeniero')])


        # Verificar si una clave existe en el diccionario
        print("¿Existe 'nombre' en el diccionario?", "nombre" in diccionario)#¿Existe 'nombre' en el diccionario? True
        #verificando si la clave "nombre" existe en el diccionario.
        #buscar entre los valores:
        print("¿Existe 'Juan' en los valores?", "Juan" in diccionario.values())  # ¿Existe 'Juan' en los valores? True


        # Fusionar dos diccionarios
        otro_diccionario = {"pais": "España", "edad": 32}  # Sobreescribe 'edad'
        diccionario.update(otro_diccionario)
        print("Después de fusionar con otro diccionario:", diccionario)#Después de fusionar con otro diccionario: {'nombre': 'Juan', 'edad': 32, 'profesion': 'Ingeniero', 'pais': 'España'}

        # Recorrer un diccionario con un bucle
        print("Recorriendo el diccionario:")
        for clave, valor in diccionario.items():
            print(f"{clave}: {valor}")

        """
            Recorriendo el diccionario:
                nombre: Juan
                edad: 32
                profesion: Ingeniero
                pais: España
        """

# Ejecutar ejemplos
DiccionariosEjemplos.ejemplos_diccionarios()


#ver ejDiccDicc.py <- es un ejemplo de un diccionario de diccionario