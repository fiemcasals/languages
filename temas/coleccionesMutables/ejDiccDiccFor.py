
# Diccionario de estudiantes, donde cada clave es un ID y el valor es otro diccionario con sus datos
estudiantes = {
    101: {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"},
    102: {"nombre": "María", "edad": 22, "carrera": "Medicina"},
    103: {"nombre": "Carlos", "edad": 21, "carrera": "Derecho"}
}

# Acceder a un diccionario dentro del diccionario
print("Datos del estudiante 101:", estudiantes[101])
#Datos del estudiante 101: {'nombre': 'Juan', 'edad': 20, 'carrera': 'Ingeniería'}

# Acceder a un valor específico dentro de un subdiccionario
print("Carrera de María:", estudiantes[102]["carrera"])
#Carrera de María: Medicina

# Agregar un nuevo estudiante
estudiantes[104] = {"nombre": "Ana", "edad": 23, "carrera": "Arquitectura"}
print("Lista actualizada de estudiantes:", estudiantes)
#Lista actualizada de estudiantes: {101: {'nombre': 'Juan', 'edad': 20, 'carrera': 'Ingeniería'}, 102: {'nombre': 'María', 'edad': 22, 'carrera': 'Medicina'}, 103: {'nombre': 'Carlos', 'edad': 21, 'carrera': 'Derecho'}, 104: {'nombre': 'Ana', 'edad': 23, 'carrera': 'Arquitectura'}}

# Modificar un valor en un subdiccionario
estudiantes[101]["edad"] = 21
print("Edad actualizada de Juan:", estudiantes[101]["edad"])
#Edad actualizada de Juan: 21

# Eliminar un estudiante
del estudiantes[103]
print("Lista después de eliminar a Carlos:", estudiantes)
#Lista después de eliminar a Carlos: {101: {'nombre': 'Juan', 'edad': 21, 'carrera': 'Ingeniería'}, 102: {'nombre': 'María', 'edad': 22, 'carrera': 'Medicina'}, 104: {'nombre': 'Ana', 'edad': 23, 'carrera': 'Arquitectura'}}


#Para recorrer todas las claves y valores:

for id_estudiante, datos in estudiantes.items():
    print(f"ID: {id_estudiante}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
    print("---")

"""
ID: 101
  nombre: Juan
  edad: 21
  carrera: Ingeniería
---
ID: 102
  nombre: María
  edad: 22
  carrera: Medicina
---
ID: 104
  nombre: Ana
  edad: 23
  carrera: Arquitectura
---
"""

#otro ejemplo 

empresa = {
    "departamento_ventas": {
        "empleado_1": {"nombre": "Luis", "edad": 30, "salario": 3000},
        "empleado_2": {"nombre": "Elena", "edad": 25, "salario": 2800}
    },
    "departamento_IT": {
        "empleado_1": {"nombre": "Carlos", "edad": 27, "salario": 3500},
        "empleado_2": {"nombre": "Sofía", "edad": 29, "salario": 4000}
    }
}

print("Salario de Sofía en el departamento IT:", empresa["departamento_IT"]["empleado_2"]["salario"])
#Salario de Sofía en el departamento IT: 4000