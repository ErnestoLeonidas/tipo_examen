import random
import json

def asignar_montos_aleatorios():
    productos = ["Café Americano",
                "Té Chai",
                "Croissant",
                "Jugo Naranja",
                "Panini de Pavo y Queso",
                "Pastel de Zanahoria",
                "Espresso Doble",
                "Batido de Frutas",
                "Muffin",
                "Ensalada",
                "Chocolate Caliente",
                "Tarta de Frambuesa",
                "Sándwich de Huevo", 
                "Galletas de Avena", 
                "Frappé de Caramelo"]
    
    todos_los_productos = []
    
    for nombre_producto in productos:
        nombre = nombre_producto
        valor_bruto = random.randint(30,80) * 100
        utilidad = int(valor_bruto * 0.4)
        iva = int(valor_bruto * 0.19)
        valor_venta = valor_bruto + utilidad + iva
        
        nuevo_producto = {
            'nombre': nombre,
            'valor_bruto': valor_bruto,
            'utilidad': utilidad,
            'iva': iva,
            'valor_venta': valor_venta
        }
        
        todos_los_productos.append(nuevo_producto)
    
    # acá guardaremos nuestros productos en un json
    guardar_archivo_json('productos.json', todos_los_productos)
    print("Valores de los productos generados.")

def guardar_archivo_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def leer_archivo_json(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def clasificar_productos():
    todos_los_productos = leer_archivo_json('productos.json')
    
    categorias = {
        'menores a $5.000': [],
        'entre $5.001 a $7.000': [],
        'superior a $ 7.001': []
    }
    
    for producto in todos_los_productos:
        if producto['valor_venta'] <= 5000:
            categorias["menores a $5.000"].append(producto)

        elif producto['valor_venta'] >= 5001 and producto['valor_venta'] <= 7000:
            categorias['entre $5.001 a $7.000'].append(producto)
        
        elif producto['valor_venta'] >= 7001:
            categorias['superior a $ 7.001'].append(producto)
    
    # recorremos cada una de las categorias, las categorias contienen los productos
    for clave, listado_productos in categorias.items():
        print("productos", clave)
        print("CANTIDAD:", len(listado_productos))
        print("Producto   Precio Venta")
        print("-----------------------")
        for producto in listado_productos:
            print(f"{producto['nombre']}  ${producto['valor_venta']}")

        print(" ")
        

        
