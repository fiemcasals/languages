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

print("\nRecorriendo un diccionario (solo valores):")
for pais in paises.values():
    print(pais)

print("\nRecorriendo un diccionario (solo claves):")
for pais in paises:
    print(pais)

print("\nRecorriendo un diccionario con claves y valores:")
for codigo, nombre in paises.items():
    print(codigo, ' -> ', nombre)
