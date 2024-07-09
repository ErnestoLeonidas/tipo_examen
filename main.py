import os
import productos
os.system("clear")

def menu_estadisticas():
    while True:
        os.system("clear")
        print("=== ESTADISTICAS ====")
        print("1. Producto con valor más alto.")
        print("2. Producto con valor del IVA más bajo.")
        print("3. Promedio del valor de los productos.")
        print("4. Media geométrica del valor de los productos")
        print("5. Salir")

        opciones = seleccionar_opcion(5)

        if opciones == 1:
            print("1. Producto con valor más alto.")
        elif opciones == 2:
            print("2. Producto con valor del IVA más bajo.")
        elif opciones == 3:
            print("3. Promedio del valor de los productos.")
        elif opciones == 4:
            print("4. Media geométrica del valor de los productos")
        elif opciones == 5:
            print("5. Salir.")
            return

        input("")

def menu_general():
    while True:
        os.system("clear")
        print("=== MENU ====")
        print("1. Asignar valores aleatorios ")
        print("2. Clasificar productos")
        print("3. Ver estadísticas.")
        print("4. Reporte de productos")
        print("5. Salir del programa")

        opciones = seleccionar_opcion(5)

        if opciones == 1:
            print("1. Asignar montos aleatorios.")
            productos.asignar_montos_aleatorios()
        elif opciones == 2:
            print("2. Clasificar productos ")
            productos.clasificar_productos()
        elif opciones == 3:
            print("3. Ver estadísticas. ")
            menu_estadisticas()
        elif opciones == 4:
            print("4. Reporte de productos ")
        elif opciones == 5:
            print("5. Salir del programa.")
            print("Desarrollado por Ernesto")
            return

        input("")

def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

menu_general()