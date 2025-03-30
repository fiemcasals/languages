/*En C, necesitarías pasar la dirección de memoria de una variable (usando `&`) cuando:

1. Estás trabajando con tipos de datos que no son punteros, y deseas modificar el valor de la variable original dentro de la función.
2. Trabajando con punteros a variables, donde quieres modificar directamente el valor de la variable original.

Aquí te doy un par de ejemplos donde es necesario usar el operador `&` para pasar la dirección de memoria de una variable.

1. Pasar la dirección de memoria de una variable (por referencia)
Si tienes una variable normal (como un `int`, `float`, etc.) y deseas modificarla dentro de una función, debes pasar su dirección para que la función pueda alterar su valor directamente.
*/

/*#include <stdio.h>

// Función que cambia el valor de la variable original
void cambiar_valor(int *x) {
    *x = 10;  // Modifica el valor en la dirección de memoria pasada
}

int main() {
    int a = 5;
    printf("Antes: %d\n", a);
    
    cambiar_valor(&a);  // Pasamos la dirección de 'a' usando '&'
    
    printf("Después: %d\n", a);  // 'a' ahora es 10
    return 0;
}*/


/*Explicación:
- `&a` pasa la dirección de memoria de la variable `a` a la función `cambiar_valor`.
- Dentro de la función, usamos `*x` para desreferenciar el puntero y modificar el valor en esa dirección de memoria.


/*
2. Pasar la dirección de una cadena de texto
En C, las cadenas de texto son punteros a un bloque de memoria donde están almacenados los caracteres. No necesitas usar `&` para pasar una cadena, pero si tienes un puntero a puntero, ahí sí sería necesario.

**Ejemplo con puntero a puntero:**
*/

/*

#include <stdio.h>

// Función que cambia la dirección de una cadena
void cambiar_cadena(char **str) {
    *str = "Nuevo texto";  // Modificamos el puntero para que apunte a otro string //Lo que se está modificando es la dirección de memoria a la que apunta el puntero.
}

int main() {
    char *cadena = "Texto original";
    printf("Antes: %s\n", cadena);
    
    cambiar_cadena(&cadena);  // Pasamos la dirección de 'cadena'
    
    printf("Después: %s\n", cadena);  // La cadena ahora es "Nuevo texto"
    return 0;
}
*/

/* Explicación:
- Aquí, `&cadena` pasa la **dirección de la variable `cadena`** a la función. La función puede luego cambiar la dirección de la cadena que apunta el puntero.

Resumen:
-Uso de `&`: Cuando deseas pasar la dirección de memoria de una variable no puntero (como un `int`, `float`, etc.), para que la función pueda modificar directamente su valor.

- No se usa `&` para punteros: Si ya estás pasando un puntero a la función, no necesitas usar `&`, ya que el puntero en sí es una dirección de memoria.
  
*/