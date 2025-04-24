# Diccionario de diccionarios de diccionarios
# Estructura: continente → país → ciudad → datos
datos_geograficos = {
    "América": {
        "Argentina": {
            "Buenos Aires": {"poblacion": 3000000, "fundacion": 1536},
            "Córdoba": {"poblacion": 1400000, "fundacion": 1573}
        },
        "Brasil": {
            "Río de Janeiro": {"poblacion": 6748000, "fundacion": 1565},
            "São Paulo": {"poblacion": 12330000, "fundacion": 1554}
        }
    },
    "Europa": {
        "España": {
            "Madrid": {"poblacion": 3266000, "fundacion": 852},
            "Barcelona": {"poblacion": 1636000, "fundacion": -15}  # Año estimado antes de Cristo
        },
        "Francia": {
            "París": {"poblacion": 2148000, "fundacion": -52},
            "Lyon": {"poblacion": 513000, "fundacion": -43}
        }
    }
}

# Ejemplos de acceso a datos:

# Acceder a todo el diccionario de un continente
print(datos_geograficos["América"])

# Acceder a todos los países dentro de Europa
print(datos_geograficos["Europa"].keys())

# Acceder a los datos de una ciudad específica
print(datos_geograficos["América"]["Argentina"]["Buenos Aires"])  # {'poblacion': 3000000, 'fundacion': 1536}

# Acceder solo a la población de São Paulo
print(datos_geograficos["América"]["Brasil"]["São Paulo"]["poblacion"])  # 12330000

# Acceder a la fundación de Lyon
print(datos_geograficos["Europa"]["Francia"]["Lyon"]["fundacion"])  # -43

# Recorrer toda la estructura de forma ordenada
for continente, paises in datos_geograficos.items():
    print(f"\n🌍 Continente: {continente}")
    for pais, ciudades in paises.items():
        print(f"  🏳️ País: {pais}")
        for ciudad, datos in ciudades.items():
            print(f"    🏙️ Ciudad: {ciudad}")
            print(f"      📊 Población: {datos['poblacion']}")
            print(f"      🗓️ Fundación: {datos['fundacion']}")
