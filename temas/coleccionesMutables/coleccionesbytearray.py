"Una colección mutable es una estructura de datos que permite modificar su contenido después de su creación. Esto significa que se pueden agregar, eliminar o cambiar elementos dentro de la colección sin necesidad de crear una nueva instancia."


class ColeccionesEjemplos:  
    @staticmethod
    def ejemplos_bytearray():
            print("--- Ejemplos con bytearray ---")
            
            # Crear un bytearray a partir de una lista de enteros
            ba = bytearray([65, 66, 67, 68])
            print("Bytearray inicial:", ba) #Bytearray inicial: bytearray(b'ABCD') #segun ASCCI
            #El prefijo b en b'ABCD' indica que la cadena es una cadena de bytes
            
            # Modificar un elemento del bytearray
            ba[2] = 88  # Cambia el 67 ('C') por 88 ('X')
            print("Bytearray después de modificar un elemento:", ba) #Bytearray después de modificar un elemento: bytearray(b'ABXD')
            
            # Agregar un valor al final con append
            ba.append(69)  # Agrega 'E'
            print("Bytearray después de append(69):", ba) #Bytearray después de append(69): bytearray(b'ABXDE')
            
            # Convertir bytearray a string
            print("Bytearray como string:", ba.decode('utf-8')) #Bytearray como string: ABXDE
            #que es utf-8? -> sistema de codificacion. caracteristicas: compatible con ASCII, usado en la web.

ColeccionesEjemplos.ejemplos_bytearray()