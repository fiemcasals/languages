"""El paradigma orientado a objetos (POO) organiza el código en clases y objetos, utilizando características como herencia, encapsulamiento y polimorfismo."""


# Definición de la clase base Persona (herencia)
class Persona:
    def __init__(self, nombre, edad):  # Constructor (inicializador de atributos)
        # Encapsulamiento: los atributos son accesibles directamente desde la clase
        self.__nombre = nombre  # El doble guion bajo indica que es un atributo privado (encapsulado)
        self.__edad = edad      # Similar al anterior, el atributo es privado

    # Método público para acceder al nombre
    def get_nombre(self):
        return self.__nombre
    
    # Método público para cambiar el nombre 
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método público para acceder a la edad
    def get_edad(self):
        return self.__edad
    
    # Método público para cambiar la edad 
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
    
    # Método de la clase (comportamiento)
    def saludar(self):
        print(f"Hola, mi nombre es {self.__nombre} y tengo {self.__edad} años.")

# Clase Estudiante que hereda de Persona (herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):  # Constructor de la clase hija
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (herencia)
        self.__carrera = carrera  # Atributo privado para encapsular la carrera

    # Método público para acceder a la carrera (accesor)
    def get_carrera(self):
        return self.__carrera
    
    # Sobrescribir el método saludar para dar más detalles (polimorfismo)
    def saludar(self):
        # Polimorfismo: la clase hija cambia el comportamiento del método de la clase base
        print(f"Hola, soy {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.__carrera}.")

# Clase Profesor que también hereda de Persona (herencia)
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):  # Constructor de la clase hija
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base (herencia)
        self.__materia = materia  # Atributo privado para encapsular la materia que enseña

    # Método público para acceder a la materia (accesor)
    def get_materia(self):
        return self.__materia
    
    # Sobrescribir el método saludar para dar más detalles (polimorfismo)
    def saludar(self):
        # Polimorfismo: cambio de comportamiento en la clase hija
        print(f"Hola, soy el Profesor {self.get_nombre()}, tengo {self.get_edad()} años y enseño {self.__materia}.")

# Crear instancias de las clases
persona1 = Persona("Juan", 30)
estudiante1 = Estudiante("Maria", 22, "Ingeniería")
profesor1 = Profesor("Carlos", 45, "Matemáticas")

# Llamar a los métodos de las clases
persona1.saludar()  # Saludo de una persona
estudiante1.saludar()  # Saludo de un estudiante (polimorfismo en acción)
profesor1.saludar()  # Saludo de un profesor (polimorfismo en acción)

# Cambiar los valores de los atributos privados usando los mutadores
estudiante1.set_nombre("Ana")
estudiante1.set_edad(23)

# Verificar que los valores se actualizaron
estudiante1.saludar()  # Nuevo saludo con el nombre actualizado

