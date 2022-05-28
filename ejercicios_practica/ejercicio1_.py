# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede inventar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    json_datos = {
                    "nombre": "Matias",
                    "apellido": "Franco",
                    "DNI": 35211531,
                    "prendas": [
                            { 
                             "prenda": "zapatillas", 
                             "cantidad": 6 
                            },
                            {
                             "prenda": "remeras", 
                             "cantidad": 10
                            },
                            {
                             "prenda": "pantalones", 
                             "cantidad": 8
                            }
                            ]
             }

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    with open('mi_datos.json', 'w') as archivo:
        datos = [json_datos]
        json.dump(datos, archivo, indent=4)

    # Observe el archivo y verifique que se almaceno lo deseado

    

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()
    
    with open('mi_datos.json', 'r') as archivo:
        datos = json.load(archivo)
        print(datos)    
    
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior
    
    json_string = json.dumps(datos, indent=4)
    print(json_string)
    
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    serializar()
    deserializar()

    print("terminamos")