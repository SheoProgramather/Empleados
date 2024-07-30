import math 
import globales

def sueldo_mas_alto():
    ventasjson = globales.leer_archivo_json('ventas.json')

    sueldo = sorted(ventasjson, key= lambda x: x['sueldo_liquido'], reverse=True)
    
    for x in sueldo[:1]:
        print(f"El sueldo liquido más ALTO corresponde a {x['nombre']} con un monto de: ${x['sueldo_liquido']}")



def sueldo_mas_bajo():
    ventasjson = globales.leer_archivo_json('ventas.json')

    sueldo = sorted(ventasjson, key= lambda x: x['sueldo_liquido'])
    
    for x in sueldo[:1]:
        print(f"El sueldo liquido más BAJO corresponde a {x['nombre']} con un monto de: ${x['sueldo_liquido']}")


def promedio_sueldos():
    ventasjson = globales.leer_archivo_json('ventas.json')

    sumados = 0 

    for sueldos in ventasjson:
        sumados += sueldos['sueldo_liquido']
        promedio = sumados / len(ventasjson)
    print(f"El promedio de sueldos liquidos es de: ${int(promedio)}")



def media_geometrica():
    ventasjson = globales.leer_archivo_json('ventas.json')

    sumados = 0 

    for sueldos in ventasjson:
        sumados += math.log(sueldos['sueldo_liquido'])
        media_geo = math.exp(sumados / len(ventasjson))
    print(f"La media geometrica de sueldos liquidos es de: ${int(media_geo)}")
