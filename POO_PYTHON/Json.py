import json

#Convertir un diccionario a Json
#Definimos el diccionario
data = {
            "Nombre": "Duvan", 
            "Edad" :  20
}

#Creamos una variable la cual me guarde la conversion a Json
Json_data=json.dumps(data)
print(Json_data)