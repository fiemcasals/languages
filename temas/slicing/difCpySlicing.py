# Problema con la asignación directa
lista_original = [1, 2, 3, 4]
lista_copiada = lista_original  # No se copia, solo se refiere

lista_copiada[0] = 99  # Cambiamos el primer elemento

print("Lista original:", lista_original)  # [99, 2, 3, 4]  (También cambia)
print("Lista copiada:", lista_copiada)   # [99, 2, 3, 4]

# Copia correcta con slicing
lista_original = [1, 2, 3, 4]
lista_copiada = lista_original[:]  # Copia con slicing

lista_copiada[0] = 99  # Solo cambia la copia

print("\nLista original tras slicing:", lista_original)  # [1, 2, 3, 4]  (Se mantiene igual)
print("Lista copiada tras slicing:", lista_copiada)   # [99, 2, 3, 4]

# Copia correcta con copy()
lista_original = [1, 2, 3, 4]
lista_copiada = lista_original.copy()

lista_copiada[0] = 99  # Solo cambia la copia

print("\nLista original tras copy:", lista_original)  # [1, 2, 3, 4]  (Se mantiene igual)
print("Lista copiada tras copy:", lista_copiada)   # [99, 2, 3, 4]

# Copia profunda con copy.deepcopy() para listas anidadas
import copy
lista_original = [[1, 2], [3, 4]]
lista_copiada = copy.deepcopy(lista_original)

lista_copiada[0][0] = 99  # Solo cambia la copia

print("\nLista original tras deepcopy:", lista_original)  # [[1, 2], [3, 4]]  (Se mantiene igual)
print("Lista copiada tras deepcopy:", lista_copiada)   # [[99, 2], [3, 4]]

#que pasa si aplico .copy no deepcopy en una lista de listas?

lista_original = [[1,2],[3,4]]
lista_copiada= lista_original.copy()

lista_copiada[0][0] = 77

print("\n lista original:", lista_original) #lista original: [[77, 2], [3, 4]]
print("\n copia lista:", lista_copiada) #copia lista: [[77, 2], [3, 4]]
#evidencia que se copia la referencia por mas que use .cpy si es una lista de listas