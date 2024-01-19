# Paso 1
import sys

umbral = float(sys.argv[1])

precios = {'Notebook': 700000,
          'Teclado': 25000,
          'Mouse': 12000,
          'Monitor': 250000,
          'Escritorio': 135000,
          'Tarjeta de Video': 1500000}

# Paso 2
def filtrar(diccionario, umbral, mayor_que = True):
    if mayor_que: # Paso 3
        filtro = [k for k,v in diccionario.items() if v > umbral]
        print(f'Los productos mayores al umbral son: {",".join(filtro)}') # Paso 4
    else: # Paso 4
        filtro = [k for k,v in diccionario.items() if v < umbral]
        print(f'Los productos menores al umbral son: {", ".join(filtro)}') # Paso 4

# Paso 5
if len(sys.argv) == 2:
    filtrar(precios, umbral)
else:
    if sys.argv[2] == 'mayor':
        filtrar(precios, umbral, True)
    elif sys.argv[2] == 'menor':
        filtrar(precios, umbral, False)
    else:
        print('Lo sentimos, no es una operación válida')
