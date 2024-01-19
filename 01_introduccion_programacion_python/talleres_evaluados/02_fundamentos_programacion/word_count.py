#abrir archivo indicando nomnbre en consola

with open('lorem_ipsum.txt', 'r') as file:
	texto=file.read()

#calculo de resultados de la lista utilizando el len y set

resultado1 = len(set(texto))
resultado2 = len(set(texto.split()))

#visualización de resultados en pantalla
print("El número de caracteres distintos es: " + str(resultado1))
print("El número de palabras distintas es: " + str(resultado2))