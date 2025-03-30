//estructurado
#include <stdio.h>

// Función que calcula la suma de los números del 1 al 5 usando punteros
void calcular_suma(int *resultado) {
    *resultado = 0;
    for (int i = 1; i <= 5; i++) {
        *resultado += i;
    }
}

// Función principal
int main() {
    int resultado;
    calcular_suma(&resultado); // Pasamos la dirección de memoria de resultado
    printf("Suma: %d\n", resultado); // Mostramos el resultado
    return 0;
}


/*Por qué es estructurado?

    Se divide el código en funciones (calcular_suma Y main).
    Cada función tiene una responsabilidad específica.
    Evita el uso de variables globales, mejorando la modularidad.*/

//en que se diferencia del paradigma funcional?

//principal diferencia: Divide en funciones, pero sigue modificando datos.(por medio de punteros a memoria). En cambio en el funcional, dentro de cada funcion, nombra sus variables (variables locales), y devuelve el resultado por medio de 'return'