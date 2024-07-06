import os
import globales
import productos
import estadisticas
os.system("cls")

def menu_estadisticas():
    while True:
        os.system("cls")
        print("=== MENU ESTADISTICAS ===")
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos.")
        print("5. salir")

        opciones = globales.seleccionar_opcion(5)

        if opciones == 1:
            estadisticas.valor_mas_alto()
        elif opciones == 2:
            estadisticas.valor_mas_bajo()
        elif opciones == 3:
            estadisticas.promedio()
        elif opciones == 4:
            estadisticas.media_geometrica()
        elif opciones == 5:
            print("5. salir")
            return
        
        input("")


def menu():
    while True:
        os.system("cls")
        print("=== MENU PRINCIPAL ===")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.2")
        print("3. Salir del programa.")

        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            productos.asignar_aleatorios()
        elif opcion == 2:
            menu_estadisticas()
        elif opcion == 3:
            print("3. Salir del programa.")
            return
        
        input("")


menu()


