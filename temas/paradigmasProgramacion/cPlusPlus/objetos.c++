/*Es un lenguaje orientado a objetos y proporciona muchas características de la programación orientada a objetos (OOP), como clases, objetos, herencia, polimorfismo y encapsulación.*/


#include <iostream>
using namespace std;

// Clase base Persona con encapsulamiento
class Persona {
private:
    string nombre;  // Atributo privado (encapsulado)
    int edad;       // Atributo privado (encapsulado)

public:
    // Constructor con parámetros
    Persona(string n, int e) : nombre(n), edad(e) {}

    // Métodos getter (accesores) para obtener los atributos
    string getNombre() const { return nombre; }
    int getEdad() const { return edad; }

    // Método setter (mutador) para cambiar el nombre
    void setNombre(const string& n) { nombre = n; }

    // Método setter (mutador) para cambiar la edad
    void setEdad(int e) { edad = e; }

    // Método de la clase base
    virtual void saludar() {
        cout << "Hola, mi nombre es " << nombre << " y tengo " << edad << " años." << endl;
    }
};

// Clase derivada Estudiante, que hereda de Persona
class Estudiante : public Persona {
private:
    string carrera;  // Atributo específico de Estudiante

public:
    // Constructor de Estudiante
    Estudiante(string n, int e, string c) : Persona(n, e), carrera(c) {}

    // Método getter para la carrera
    string getCarrera() const { return carrera; }

    // Sobrescritura del método saludar (polimorfismo)
    void saludar() override {
        cout << "Hola, soy " << getNombre() << ", tengo " << getEdad() << " años, y estudio " << carrera << "." << endl;
    }
};

// Clase derivada Profesor, que hereda de Persona
class Profesor : public Persona {
private:
    string materia;  // Atributo específico de Profesor

public:
    // Constructor de Profesor
    Profesor(string n, int e, string m) : Persona(n, e), materia(m) {}

    // Método getter para la materia
    string getMateria() const { return materia; }

    // Sobrescritura del método saludar (polimorfismo)
    void saludar() override {
        cout << "Hola, soy el Profesor " << getNombre() << ", tengo " << getEdad() << " años, y enseño la materia de " << materia << "." << endl;
    }
};

int main() {
    // Creación de objetos de las clases derivadas
    Persona p1("Juan", 30);  // Objeto de la clase Persona
    p1.saludar();  // Llamamos al método saludar de Persona

    Estudiante e1("Ana", 20, "Ingeniería Informática");  // Objeto de la clase Estudiante
    e1.saludar();  // Llamamos al método saludar de Estudiante (polimorfismo)

    Profesor prof1("Carlos", 45, "Matemáticas");  // Objeto de la clase Profesor
    prof1.saludar();  // Llamamos al método saludar de Profesor (polimorfismo)

    return 0;
}
