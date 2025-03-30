
/*2. Paradigma Estructurado en C:

El paradigma estructurado se enfoca en dividir el programa en bloques de códigos, como funciones, para promover la claridad y legibilidad.
Habiamos visto anteriormente, que trabajaba "principalmente" con punteros o direcciones de memoria a diferencia del funcional*, pero que en la practica era muy similar*/

#include <iostream>
using namespace std;

// Función que calcula la suma de dos números
int sumar(int a, int b) {
    return a + b;
}

int main() {
    int resultado = sumar(5, 3);  // Llamamos a la función para calcular la suma
    cout << "La suma es: " << resultado << endl;
    return 0;
}
