import sys
#ingreso de datos por medio de argv
sol=float(sys.argv[1])
peso_argentino=float(sys.argv[2])
dolar=float(sys.argv[3])
peso_chileno=int(sys.argv[4])

#calculo y visualización por pantalla de los resultados
print("Los {:,} pesos que equivalen a: ".format(peso_chileno))
print("{:.1f} Soles".format(sol*peso_chileno))
print("{:.1f} Pesos Argentinos".format(peso_argentino*peso_chileno))
print("{:.1f} Dólares".format(dolar*peso_chileno))	