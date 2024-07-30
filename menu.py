import os 
import globales
import ventas
import estadisticas
import reporte

def menu_estadisticas():
    while True:
        print("=== ESTADISTICAS ===")
        print("1. Sueldo mas alto")
        print("2. Sueldo mas bajo")
        print("3. Promedio sueldos")
        print("4. Media geometrica")
        print("5. Volver a menú principal")
        
        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            os.system("cls")
            print("1. Sueldo mas alto")
            estadisticas.sueldo_mas_alto()

        elif opcion == 2:
            os.system("cls")
            print("2. Sueldo mas bajo")
            estadisticas.sueldo_mas_bajo()

        elif opcion == 3:
            os.system("cls")
            print("3. Promedio sueldos")
            estadisticas.promedio_sueldos()

        elif opcion == 4:
            os.system("cls")
            print("4. Media geometrica")
            estadisticas.media_geometrica()

        elif opcion == 5:
            os.system("cls")
            print("5. Volver a menú principal")
            menu()
            
        input()

def menu():
    while True:
        os.system("cls")
        print("=== MENU PRINCIPAL ===")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = globales.seleccionar_opcion(5)

        if opcion == 1:
            os.system("cls")
            print("1. Asignar sueldos aleatorios")
            ventas.Asignar_sueldos_aleatorios()

        elif opcion == 2:
            os.system("cls")
            print("2. Clasificar sueldos")
            ventas.Clasificar_sueldos()

        elif opcion == 3:
            os.system("cls")
            print("3. Ver estadisticas")
            menu_estadisticas()

        elif opcion == 4:
            print("4. Reporte de sueldos")
            reporte.reporte_sueldos()
        elif opcion == 5:
            print("5. Salir")
            print("Desarrollado por Sergio Velásquez Ramírez")
            print("Rut 20.160.758-2")
            return
        input()

if __name__ == "__main__":
    menu()