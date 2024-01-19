import requests
import json
import pandas as pd
from string import Template

'''Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla -- Función'''
def obtencion(url):
    payload = ""
    headers = ""

    respuesta1 = requests.request("GET",url, data = payload, headers = headers)
    print(respuesta1.status_code)
    return json.loads(respuesta1.text)

'''Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
diccionario de respuesta en una variable llamada created_user e imprímala en
pantalla -- Función'''

def creacion(url):
    payload = ""
    headers = ""
    post_data = {"name": "Ignacio",
            "job": "Profesor"}
   
    respuesta2 = requests.request("POST",url, data = post_data, headers = headers)
    print(respuesta2.status_code)
    return json.loads(respuesta2.text)

'''Actualice un usuario llamado morpheus para que tenga un campo llamado igual a zion. Guarde el diccionario de respuesta en una variable llamada
e imprímala en pantalla. /// usuario Morpheus no existe, se cambiara cualquier otro. Campo residence no existe, se cambiara cualquier otro -- Función'''

def actualizacion(url):
    datos1 = {'name':'morpheus', 'address': 'zion'}
    payload_dict = {'first_name': ['Charles', 'Morpheus']}
    headers = ""
    respuesta3 = requests.request("PATCH",url + '/id=5', data=payload_dict, headers = headers)
    print(respuesta3.status_code)
    return json.loads(respuesta3.text)

def eliminacion(url):
    headers = ""
    data_delete= {'first_name':'Tracey'}
    respuesta4 = requests.request("DELETE",url, data = data_delete ,headers = headers)
    print(respuesta4.status_code)
    #return json.loads(respuesta4.text)

url = "https://reqres.in/api/users"




'''Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla -- Impresión'''
users_data = obtencion(url)
print(users_data)

'''Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el diccionario de respuesta 
en una variable llamada created_user e imprímala en pantalla. -- Impresión'''
create_user = creacion(url)
print(create_user)

'''Actualice un usuario llamado morpheus para que tenga un campo llamado igual a zion. Guarde el diccionario de respuesta en una variable llamada
e imprímala en pantalla. -- Impresión'''
updated_user = actualizacion(url)
print(updated_user)

'''Actualice un usuario llamado morpheus para que tenga un campo llamado igual a zion. Guarde el diccionario de respuesta en una variable llamada
e imprímala en pantalla. -- Impresión'''
delete_user = eliminacion(url)
#print(delete_user)