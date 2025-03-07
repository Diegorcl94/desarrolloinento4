import json
import math
import globales

def promedio():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    suma = 0
    cantidad = 0

    for producto in todos_los_productos:
        suma += producto['valor']
        cantidad += 1

    average = int(suma/cantidad)
    
    print(f"el promedio del valor de los productos es: ${average}")


def media_geometrica():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    suma = 0
    cantidad = 0

    for producto in todos_los_productos:
        suma += math.log(producto['valor'])
        cantidad += 1

    average = math.exp(suma/cantidad)

    print(f"la media geometrica del valor de los productos es: ${int(average)}")


def valor_mas_alto():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    productos_ordenados = sorted(todos_los_productos, key=lambda x: x['valor'], reverse=True)

    for producto in productos_ordenados[:1]:
        print(f"el prodcuto con el valor más alto es {producto['nombre']}: ${producto['valor']}")
        return
    

def valor_mas_bajo():
    todos_los_productos = globales.leer_archivo_json("productos.json")

    productos_ordenados = sorted(todos_los_productos, key= lambda x: x['iva'], reverse=False)

    for producto in productos_ordenados[:1]:
        print(f"el producto con el valor del iva más bajo es {producto['nombre']}: ${producto['iva']}")
        return
    
valor_mas_bajo()