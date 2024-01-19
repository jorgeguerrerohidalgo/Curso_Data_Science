
import requests
import json
import pandas as pd
from string import Template


def request(url):
    ''' paremetros:
        1.- metodo: recibe un str, con los distintos valores de la funcion
        requets, que es: 'GET'
        2.- url: recibe un str, con la dirección http para conectarse a la api + apikey
        3.- data: para colocar nueva data en el parametro payload del request'''
    payload = ""
    headers = headers = {"api_key" : "nEHGRkWBTOle5mW9SzvvLlOvd1R1klsfNo7TSYvb"}

    response = requests.request("GET",url, data = payload, headers = headers)
    return json.loads(response.text)

def build_web_page(z):
    ''' paremetros:
        1.- funcion: recibe una lista, con las url de las 25 fotografias obtenidas del request y posteriormente filtradas del ciclo for=i in range(25)'''
    img_template = Template('<img src="$url">')
    imagen = img_template.substitute(url = 'Hola')
        #print(imagen)
    html_template = Template('''<!DOCTYPE html>
                                <html>
                                <head>
                                <title>Prueba API NASA - Jorge Guerrero Hidalgo</title>
                                </head>
                                <body>

                                <h1>Prueba API NASA - Jorge Guerrero Hidalgo</h1>

                                $body

                                </body>
                                </html>
                            ''')
    #print(html_template.substitute(body = imagen))
    texto_img = ''
    for url in z:
        texto_img += img_template.substitute(url = url) +'\n'
            
    #print(texto_img)

    html = html_template.substitute(body = texto_img)
    #print(html)

    with open('output.html', 'w') as f:
        f.write(html)


url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?sol=1000&api_key=nEHGRkWBTOle5mW9SzvvLlOvd1R1klsfNo7TSYvb"



results = request(url)
z=[]
for i in range(25):
    x= results["latest_photos"][i]["img_src"]
    z.append(x)

build_web_page(z)


