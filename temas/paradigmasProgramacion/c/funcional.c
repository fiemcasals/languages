#include <stdio.h>

// Función pura que calcula la suma de los números del 1 al 5
int calcular_suma(int numeros[], int tamanio) {
    int suma = 0;
    for (int i = 0; i < tamanio; i++) {
        suma += numeros[i];
    }
    return suma;
}

// Función principal
int main() {
    int numeros[] = {1, 2, 3, 4, 5}; // Array de números
    int resultado = calcular_suma(numeros, 5); // Llamamos a la función con el array y su tamaño
    printf("Suma: %d\n", resultado); // Mostramos el resultado
    return 0;
}
