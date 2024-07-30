import json 
import globales
import random
import math

def Asignar_sueldos_aleatorios():
    ventasjson = globales.leer_archivo_json('ventas.json')

    trabajadores = ['Juan Perez', 'Maria Garcia', 'Carlos Lopez', 'Ana Martinez', 'Pedro Rodriguez', 'Laura Hernandez', 'Miguel Sanchez', 'Isabel Gomez', 'Francisco Diaz', 'Elena Fernandez']

    ventasjson = []

    for sueldos in range(10):
        nombre = random.choice(trabajadores)
        sueldo_base = random.randint(3000, 25000) * 100
        descuento_afp = int(sueldo_base * 0.07)
        descuento_salud = int(sueldo_base * 0.12)
        total_descuentos = int(descuento_afp + descuento_salud)
        sueldo_liquido = int(sueldo_base - total_descuentos)
        
        ventasjson.append({
            "nombre": nombre,
            "sueldo_base": sueldo_base,
            "descuento_afp": descuento_afp,
            "descuento_salud": descuento_salud,
            "total_descuentos": total_descuentos,
            "sueldo_liquido": sueldo_liquido
        })

    globales.guardar_archivo_json('ventas.json', ventasjson)
    print("1O Sueldos creados de forma aleatoria listo!")



def Clasificar_sueldos():
    ventasjson = globales.leer_archivo_json('ventas.json')

    categorias = {
        'Sueldos menores a $800.000': [],
        'Sueldos entre $800.000 y $2.000.000': [],
        'Sueldos superiores a $2.000.000': []
    }

    
    for sueldos in ventasjson:
        if sueldos['sueldo_liquido'] <= 800000:
            categorias['Sueldos menores a $800.000'].append(sueldos)
        elif sueldos['sueldo_liquido'] >= 800001 and sueldos['sueldo_liquido'] <= 2000000:
            categorias['Sueldos entre $800.000 y $2.000.000'].append(sueldos)
        elif sueldos['sueldo_liquido'] >= 2000001:
            categorias['Sueldos superiores a $2.000.000']
    for clave, valor in categorias.items():
        print(f"{clave} | Total: {len(valor)}")
        print("Nombre empleado\t\t\tSueldo")
        for sueldos in valor:
            print(f"{sueldos['nombre']}\t\t\t${sueldos['sueldo_liquido']}")
        print("----------------------------------------")
    suma = 0   
    for sueldos in ventasjson:
        suma += sueldos['sueldo_liquido']
    print(f"TOTAL SUELDOS: ${suma}")
            #     sueldo += x['sueldo_liquido']
            # # print(x)

        

