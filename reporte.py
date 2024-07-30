import json 
import globales


def reporte_sueldos():

    ventasjson = globales.leer_archivo_json('ventas.json')

    print("Nombre empleado\t|Sueldo base\t|Descuento salud\t|Descuento afp\t|Sueldo Liquido")
    for sueldo in ventasjson:
        print(f"{sueldo['nombre']}\t|$ {sueldo['sueldo_base']}\t|$ {sueldo['descuento_afp']}\t\t|$ {sueldo['descuento_salud']}\t|$ {sueldo['sueldo_liquido']}")


    fieldnames = ['nombre', 'sueldo_base', 'descuento_afp', 'descuento_salud', 'total_descuentos', 'sueldo_liquido']
    globales.guardar_archivo_csv("sueldos.csv", ventasjson, fieldnames)
