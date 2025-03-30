"""Colecciones inmutables: específicamente en relación con tuplas y strings, y cómo estos tipos permiten usar plantillas o templates."""


class ColeccionInmutable:
    def __init__(self):
        # Ejemplo de uso de string inmutable con formato
        self.materia = "Bienvenidos a {0}, somos {1} alumnos".format("Paradigmas II", "36")
        
        # Ejemplo de tuplas (inmutables)
        self.tupla_original = (12, "asd", 23)
        self.tupla_nueva = ()  # Inicializamos la variable correctamente

        # Se puede definir la tupla sin paréntesis también
        # self.tupla_original = 12, "asd", 23
        self.a, self.b, self.c = self.tupla_original  # Desempaquetando la tupla en variables
    
    def mostrar_materia(self):
        # Muestra el string con formato
        print(self.materia)
    
    def cambiar_valores_tupla(self):
        # Intentamos cambiar el valor de la tupla (esto fallará porque las tuplas son inmutables)
        try:
            self.tupla_original[0] = 99  # Esto dará un error
        except TypeError as e:
            print(f"Error al intentar modificar tupla: {e}")
    
    def cambiar_tupla(self):
        # Reasignamos valores a nuevas variables
        self.a, self.b, self.c = self.c, self.a, self.b
        print(f"Después de cambiar la tupla: a = {self.a}, b = {self.b}, c = {self.c}")
    
    def mostrar_tupla(self):
        # Muestra los valores de la tupla original
        print(f"Tupla original: {self.tupla_original}")
        print(f"Valores desempaquetados: a = {self.a}, b = {self.b}, c = {self.c}")

    def mostrar_tupla_nueva(self):
        # Muestra los valores de la nueva tupla creada
        print(f"Tupla nueva: {self.tupla_nueva}")
     
    def nueva_tupla(self):
        # Creamos una nueva tupla con los valores actuales
        self.tupla_nueva = (self.a, self.b, self.c)

    def pisar_tupla(self, a,b,c):
        #voy a pisar los valores de nueva tupla con a,b y c
        self.tupla_nueva=(a,b,c)
        self. tupla_nueva = (a+1,b+1,c+1)



# Crear una instancia de la clase
coleccion = ColeccionInmutable()

# Mostrar el string formateado
coleccion.mostrar_materia()

# Intentar cambiar un valor dentro de la tupla (esto fallará)
coleccion.cambiar_valores_tupla()

# Cambiar el orden de los elementos de la tupla y mostrar el resultado
coleccion.cambiar_tupla()

# Mostrar los valores actuales de la tupla original
coleccion.mostrar_tupla()

# Generar una nueva tupla con los valores cambiados
coleccion.nueva_tupla()

# Mostrar los valores de la nueva tupla
coleccion.mostrar_tupla_nueva()

coleccion.pisar_tupla(1,2,3)

coleccion.mostrar_tupla_nueva()


"""nota:

   tupla3 = tuple([1, 2, 3])  # Convierte una lista en tupla

Las tuplas no se pueden editar porque no tienen métodos como `.append()` o `.remove()` que sí tienen las listas.


¿Cómo verificar si una variable es una tupla?
Podemos usar `type()` o `isinstance()`:


tupla = (1, 2, 3)
print(type(tupla))  # <class 'tuple'>

print(isinstance(tupla, tuple))  # True


¿Qué diferencia una tupla de una lista?
| Característica    | Tupla `tuple`                    | Lista `list`                         |

|   Mutable         | ❌ No                            | ✅ Sí                                 |
|   Sintaxis        | `(1, 2, 3)`                      | `[1, 2, 3]`                           |
|   Modificación    | No se puede modificar            | Se pueden agregar/eliminar elementos |
|   Velocidad       | Más rápida                       | Más lenta                            |
|   Uso recomendado | Datos constantes o estructurados | Datos dinámicos o modificables       |



### **¿Cómo modificar una tupla indirectamente?**
Si realmente necesitas modificar una tupla, puedes convertirla en una **lista**, modificarla y volver a convertirla en una tupla:


tupla = (1, 2, 3)
lista = list(tupla)  # Convertimos a lista
lista[0] = 100       # Modificamos el valor
tupla_modificada = tuple(lista)  # Volvemos a convertir en tupla
print(tupla_modificada)  # (100, 2, 3)

"""