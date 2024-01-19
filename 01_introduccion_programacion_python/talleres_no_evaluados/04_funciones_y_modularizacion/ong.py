# FUNCIÓN FACTORIAL
def factorial(valor):
    x = 1
    for i in range(1,valor+1):
        x = x*i  
    return x

# FUNCIÓN PRODUCTORIA
def productoria(lista):
    z=1
    for y in lista:
        z = z * y  
    return z

# FUNCIÓN PARA DECIDIR EN BASE AL TIPO DE DATO, EL ASTERÍSCO ** IDENTIFICA EL ARGUMENTO KWARGS (KEYBOARD ARGUMENTS)
def calcular(**parametros):
    for key, value in parametros.items():
        if type(value) == int:
            print(f"El factorial de {value} es {factorial(value)}")

        elif type(value) == list:
            print(f"La productoria de {value} es {productoria(value)}")

        else:
            print("Nadita")         

calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)