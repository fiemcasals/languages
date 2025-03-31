#otra metodologia de else, sin if: (una vez que se agota el for) ->logica: trabaja con True o False

paises = {
'AR': 'Argentina',
'BR': 'Brasil',
'EU': 'Estados Unidos'
}

for codigo, nombre in paises.items():
    print(codigo, ' -> ', nombre)
else:
    print("Fin de la iteración, SIN BREAK")