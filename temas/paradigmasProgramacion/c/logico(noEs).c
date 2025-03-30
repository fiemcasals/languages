/*El paradigma lógico es mejor representado por lenguaje como Prolog, que ya está basado en en las reglas y resultados lógicos.
Es decir, el programa corre como estructurado y llega a analizar reglas(similar a ejecutar funciones), en base a eso da una respuesta. En c se pueden imitar esas reglas usando funciones. pero no es el paradigma propiamente dicho */


//simulacion en c: Este ejemplo simula una simple base de hechos y reglas para determinar si una persona es un progenitor de otra (padre o madre).

#include <stdio.h>
#include <string.h>

// Hechos: Relaciones padre e hijo
int es_padre(const char *padre, const char *hijo) {
    // Definimos algunas relaciones de hechos
    if (strcmp(padre, "Juan") == 0 && strcmp(hijo, "Maria") == 0) {
        return 1; // Juan es padre de Maria
    }
    if (strcmp(padre, "Juan") == 0 && strcmp(hijo, "Jose") == 0) {
        return 1; // Juan es padre de Jose
    }
    return 0; // No hay relación padre-hijo en el hecho
}

int es_madre(const char *madre, const char *hijo) {
    // Definimos algunas relaciones de hechos
    if (strcmp(madre, "Ana") == 0 && strcmp(hijo, "Maria") == 0) {
        return 1; // Ana es madre de Maria
    }
    if (strcmp(madre, "Ana") == 0 && strcmp(hijo, "Jose") == 0) {
        return 1; // Ana es madre de Jose
    }
    return 0; // No hay relación madre-hijo en el hecho
}

// Regla: Progenitor es alguien que sea padre o madre de una persona
int es_progenitor(const char *persona, const char *hijo) {
    if (es_padre(persona, hijo) || es_madre(persona, hijo)) {
        return 1; // Persona es progenitor
    }
    return 0; // Persona no es progenitor
}

int main() {
    const char *persona = "Juan";
    const char *hijo = "Maria";

    if (es_progenitor(persona, hijo)) { //si surge la duda de la posicion de memoria, ver abajo
        printf("%s es progenitor de %s.\n", persona, hijo);
    } else {
        printf("%s no es progenitor de %s.\n", persona, hijo);
    }

    return 0;
}



/*no es necesario usar & porque persona es un puntero del tipo const char *
    //En C, las cadenas de texto son punteros a un bloque de memoria donde se almacenan los caracteres. 
    //si yo paso con & una cadena que dijimos q es un puntero, yo en realidad estoy pasando la direccion de memoria de un puntero. Se usa para que el puntero apunte a otra direccion de memoria. (hay que verlo en una clase con ejemplos)*/