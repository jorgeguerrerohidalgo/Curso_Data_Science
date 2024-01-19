from string import ascii_lowercase

password =str(input('Ingrese la contraseña: ')).lower()
letras=ascii_lowercase
intento=0

for recorrido_pass in password:
    for recorrido_letras in letras:
        intento+=1
        if recorrido_pass==recorrido_letras:
            break

            
print ('La contraseña fue forzada en: ',(intento), 'intentos')