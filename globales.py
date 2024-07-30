import json 
import csv

def guardar_archivo_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)
    

def guardar_archivo_csv(dir, data, fieldnames):
    with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
        data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
        data_csv.writeheader()
        data_csv.writerows(data)


def seleccionar_opcion(max_value):
    while True:
        try:
            opcion = int(input("Ingrese una opción > "))
        except:
            print("Ingrese una opción valida. Presione >>ENTER<< para continuar.")
        if opcion < 1 or opcion > max_value:
            input("Opcion invalida, intente nuevamente > ")
        else:
            return opcion
                