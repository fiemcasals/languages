# Lista de ciudades
ciudades = ['Buenos Aires', 'Río de Janeiro', 'Denver']

print("Recorriendo una lista con for:")
for ciudad in ciudades:
    print(ciudad)

print("\nUsando enumerate para obtener el índice:")
for indice, ciudad in enumerate(ciudades):
    print(indice, ' - ' + ciudad)

print("\nUsando enumerate con un índice personalizado:")
for indice, ciudad in enumerate(ciudades, start=100):
    print(indice, ' - ' + ciudad)

# Diccionario de países
paises = {
    'AR': 'Argentina',
    'BR': 'Brasil',
    'EU': 'Estados Unidos'
}

print("\nRecorriendo un diccionario (solo claves):")
for pais in paises:
    print(pais)

print("\nRecorriendo un diccionario con claves y valores:")
for codigo, nombre in paises.items():
    print(codigo, ' -> ', nombre)


# Diccionario de países con diccionarios internos
paises = {
    'AR': {
        'nombre': 'Argentina',
        'poblacion': 47000000
    },
    'BR': {
        'nombre': 'Brasil',
        'poblacion': 215000000
    },
    'EU': {
        'nombre': 'Estados Unidos',
        'poblacion': 331000000
    }
}

# Primer FOR: recorre las claves del diccionario principal
for codigo, info in paises.items():
    print(f"🌎 Código: {codigo}")
    
    # Segundo FOR: recorre el diccionario interno (nombre y poblacion)
    for clave, valor in info.items():
        print(f"   {clave.capitalize()}: {valor}")

"""Salida"""

"""
🌎 Código: AR
   Nombre: Argentina
   Poblacion: 47000000
🌎 Código: BR
   Nombre: Brasil
   Poblacion: 215000000
🌎 Código: EU
   Nombre: Estados Unidos
   Poblacion: 331000000
"""