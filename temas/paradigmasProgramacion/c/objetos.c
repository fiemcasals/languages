/*El paradigma orientado a objetos (OOP) no está directamente soportado en C, ya que C es un lenguaje procedural. Sin embargo, puedes simular algunos aspectos de la programación orientada a objetos utilizando estructuras (`struct`) y punteros para crear algo similar a clases y objetos.

En este ejemplo, crearemos una "clase" en C utilizando estructuras y funciones que operan sobre esas estructuras. Simularemos métodos y atributos para una clase llamada `Persona`, donde se puede establecer y obtener el nombre y la edad de una persona.*/

#include <stdio.h>
#include <stdlib.h> //usado normalmente para administrar memoria dinamicamente
#include <string.h>

// Definición de la "clase" Persona (simulada con struct)
typedef struct {
    char nombre[50];
    int edad;

    // Métodos (funciones que operan sobre la estructura)
    void (*set_nombre)(struct Persona*, const char*); //no devuelve nada, define el puntero a la funcion, y define las variables de las funciones, con sus tipos de datos
    void (*set_edad)(struct Persona*, int);
    void (*mostrar_info)(struct Persona*);
} Persona;

// Función que establece el nombre
void set_nombre(Persona* p, const char* nombre) {
    strncpy(p->nombre, nombre, sizeof(p->nombre) - 1);//"sizeof(p->nombre) - 1" asegura que no quiera copiar un nombre mas grande que el tamanio de la variable "50"
    p->nombre[sizeof(p->nombre) - 1] = '\0'; // Asegurarse de que la cadena esté terminada. determina hasta donde leer
}

// Función que establece la edad
void set_edad(Persona* p, int edad) {
    p->edad = edad;
}

// Función que muestra la información de la persona
void mostrar_info(Persona* p) {
    printf("Nombre: %s\n", p->nombre);
    printf("Edad: %d\n", p->edad);
}

// Función para crear una nueva Persona
Persona* crear_persona(const char* nombre, int edad) {
    Persona* p = (Persona*)malloc(sizeof(Persona));
    if (p == NULL) {
        printf("Error al asignar memoria.\n");
        return NULL;
    }

    // Inicializar los métodos
    p->set_nombre = set_nombre;
    p->set_edad = set_edad;
    p->mostrar_info = mostrar_info;

    // Establecer los valores iniciales
    p->set_nombre(p, nombre);
    p->set_edad(p, edad);

    return p;
}

// Función para liberar la memoria
void destruir_persona(Persona* p) {
    free(p);
}

int main() {
    // Crear una persona usando la "clase"
    Persona* persona1 = crear_persona("Juan", 25);
    
    // Usar los métodos de la "clase"
    persona1->mostrar_info(persona1);

    // Modificar los atributos de la persona
    persona1->set_nombre(persona1, "Carlos");
    persona1->set_edad(persona1, 30);
    
    // Mostrar la nueva información
    persona1->mostrar_info(persona1);

    // Liberar memoria
    destruir_persona(persona1);

    return 0;
}


/* Explicación:
1. **Estructura `Persona`**: Es una simulación de una clase en C. Dentro de la estructura, tenemos dos atributos (`nombre` y `edad`) y tres punteros a funciones, que simulan los métodos de una clase.
   
2. Métodos: Las funciones `set_nombre`, `set_edad` y `mostrar_info` son las que modifican y muestran los atributos de la "clase". Estas funciones se asignan a los punteros de funciones dentro de la estructura `Persona`.

3. `crear_persona`: Esta función crea una nueva instancia de `Persona` (un "objeto" de la clase `Persona`), asignando memoria dinámica para la estructura y configurando sus métodos.

4. Uso en `main`: Creamos una "instancia" de la "clase" `Persona`, usamos sus métodos para modificar sus atributos y mostrar su información. Al final, liberamos la memoria asignada.

¿Qué hemos simulado aquí?
- Clases: Usamos `struct` para simular clases.
- Objetos: Creamos instancias de `Persona` mediante `malloc` (memoria dinámica).
- Métodos: Usamos punteros a funciones dentro de la estructura para simular métodos.
- Encapsulación: Los datos (`nombre` y `edad`) están encapsulados dentro de la estructura `Persona` y sólo pueden ser modificados mediante las funciones asociadas.

Limitaciones de C:
Aunque este enfoque simula la programación orientada a objetos, no tiene algunas características que se encuentran en lenguajes con soporte nativo para OOP, como la herencia, el polimorfismo, y la sobrecarga de métodos. Sin embargo, este enfoque básico puede ser útil para simular OOP en C, especialmente cuando se requiere organización y modularidad en el código.*/