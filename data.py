import json
from prueba import js


data = js

# ESCRIBIR FORMATO JSON
with open("data.json", "w") as file:
    json.dump(data, file)

# LEER FORMATO JSON
with open("data.json", "r") as file:
    json.load(file)
