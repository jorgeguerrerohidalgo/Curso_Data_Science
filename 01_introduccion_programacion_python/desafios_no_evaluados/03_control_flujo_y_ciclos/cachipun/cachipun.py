#importar librerias
import sys
import random

#ingreso de opción del jugador por consola
jugador = sys.argv[1].lower()

if (jugador != 'piedra' and jugador != 'papel' and jugador != 'tijera'):
    print ('Argumento Invalido: Debe ser piedra, papel o tijera.')
else:
    aleatorio= random.choice(['piedra','papel','tijera'])
    
    print(f'''
    Tu jugaste {jugador},
    Computador jugó {aleatorio}''')
    
    if (jugador == 'piedra' and aleatorio == 'tijera') or (jugador=='tijera' and aleatorio=='papel') or (jugador=='papel' and aleatorio=='piedra'):
        print('Felicitaciones has ganado!!!!')
    elif jugador==aleatorio:
        print('Has empatado con la computadora...')
    else:
        print('Perdiste....')
        
            