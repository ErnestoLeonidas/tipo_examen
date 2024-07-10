import math
import json
import productos

def generar_promedios():
    todos_los_productos = productos.leer_archivo_json("productos.json")
    
    sumar_cantidades = 0
    
    for producto in todos_los_productos:
        sumar_cantidades += producto['valor_venta']
    
    promedio = sumar_cantidades/len(todos_los_productos)
    
    print(f"El promedio del valor de venta de los productos es ${int(promedio)}")


def generar_media_geometrica():
    todos_los_productos = productos.leer_archivo_json("productos.json")
    
    sumar_cantidades = 0
    
    for producto in todos_los_productos:
        sumar_cantidades += math.log(producto['valor_bruto'])
    
    promedio = math.exp(sumar_cantidades/len(todos_los_productos))
    
    print(f"La media geometrica del valor bruto de los productos es ${int(promedio)}")

def obtener_mas_alto():
    todos_los_productos = productos.leer_archivo_json("productos.json")
    
    productos_ordenados = sorted(todos_los_productos, key=lambda x: x['valor_venta'], reverse=True)
    
    for producto in productos_ordenados[:1]:
        print("El producto con valor más alto es:", producto['nombre'])
        print("y su valor es: $", producto['valor_venta'])

def obtener_mas_bajo():
    todos_los_productos = productos.leer_archivo_json("productos.json")
    
    productos_ordenados = sorted(todos_los_productos, key=lambda x: x['valor_venta'], reverse=False)
    
    for producto in productos_ordenados[:1]:
        print("El producto con valor más bajo:", producto['nombre'])
        print("y su valor es: $", producto['valor_venta'])
