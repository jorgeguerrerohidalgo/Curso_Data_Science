
# from re import I

rut_lista = []
dv = [3,2,7,6,5,4,3,2]
def string_int(my_data):
    for i in my_data:
        rut_lista.append(int(i))
    #print (rut_lista)

rut_usuario = input('Ingrese su RUT sin puntos, guión y digito verificador: ')
string_int(rut_usuario)

lista_multiplicada = [x*y for x,y in zip(rut_lista,dv)]
#print (dv)
#print (lista_multiplicada)
suma=0
for x in lista_multiplicada:
    suma += x

#print (suma)

resto= 11-(suma %11)
#print (resto)
if resto ==10:
    print ('El digito verificador es: K')
elif resto==11:
    print ('El digito verificador es: 0')
else:
    print ('El digito verificador es: ',resto)



