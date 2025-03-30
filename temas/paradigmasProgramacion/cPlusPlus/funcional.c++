/*Paradigma Funcional en C.

Características funcionales, como las funciones de orden superior y el uso de lambdas (difusión anónimas).*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> numeros = {1, 2, 3, 4, 5};
    
    // Usamos un lambda para transformar los elementos del vector
    transform(numeros.begin(), numeros.end(), numeros.begin(), [](int x) { return x * 2; });
    
    // Imprimimos los números transformados
    for (int num : numeros) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}

/*En este ejemplo, estamos utilizando un lambda (una función) comulministrada para aplicar una operación funcional sobre cada elemento del vector.*/