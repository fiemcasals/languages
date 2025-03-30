/*Paradigma Lógico en C++

Aunque C++ no es un lenguaje lógico como Prolog, se aplican ciertos enfoques lógicos utilizando estructuras como la programación declarativa con condiciones y reglas. Sin embargo, no es tan natural como en un lenguaje como Prolog. C++ no está orientado a la lógica programación de forma explícita.*/

#include <iostream>
using namespace std;

bool es_progenitor(int edad_padre, int edad_hijo) {
    return edad_padre > edad_hijo;  // Lógica simple de progenitor
}

int main() {
    int padre = 40;
    int hijo = 20;
    
    if (es_progenitor(padre, hijo)) {
        cout << "El padre puede ser progenitor del hijo." << endl;
    } else {
        cout << "El padre no es progenitor del hijo." << endl;
    }
    
    return 0;
}

//ver ejemplo de prolog para entender como se deberian aplicar las reglas