from math import sqrt

# Definición de variables de entrada y consultas a usuario
gravitacional = float(input("Ingrese la constante gravitacional en m/s2: "))
radio = int(input("Ingrese el radio de la tierra en Km: "))
radio_metros = radio * 1000

# Proceso
velocidad_escape = sqrt(2*(gravitacional * radio_metros))

# Variable con funcion round para calibrar la salida esperada
velocidad = round(velocidad_escape, 2)

# Salida
print(f"La velocidad de escape es {velocidad} [m/s]")