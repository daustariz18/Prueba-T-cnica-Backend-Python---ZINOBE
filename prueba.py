import requests
import pandas as pd
from time import time
from hashlib import sha1

url = "https://restcountries.com/v3.1/all"
data = requests.get(url)
paises = data.json()
lenguaje = []
country = []
region = []
encriptar = []
tiempo = []
key_Error = 0
cont = False


for pais in paises:
    # Region
    tiempo_inicial = time()
    region.append(pais['region'])
    # Pais
    country.append(pais['name']['common'])
    # Idiomas
    try:
        idiomas = pais['languages']
        for idioma in idiomas:
            if cont is False:
                idioma_select = idiomas[idioma]
                psw = sha1(idioma_select.encode('utf-8')).hexdigest()
                lenguaje.append(idiomas[idioma])
                encriptar.append(psw)
                tiempo_final = time()
                tiempo_ejecucion = tiempo_final - tiempo_inicial
                tiempo.append(tiempo_ejecucion)
                cont = True
            else:
                break
    except KeyError:
        key_Error += 1
    cont = False

user_list = list(zip(region, country, encriptar, tiempo))
# TABLA EN PANDA
tabla = pd.DataFrame(user_list, columns=['Region', 'Pais', 'Idioma', 'Tiempo'])
# JSON GENERADO
js = tabla.to_json(orient='records')


'''
print(js)
print("número de Key_Erroneas: " + str(key_Error))
print("Total de Regiones: " + str(len(region)))
print("Total de Regiones:" + str(len(country)))
print("Total de Regiones:" + str(len(lenguaje)))
print("Total de Regiones:" + str(len(encriptar)))
'''