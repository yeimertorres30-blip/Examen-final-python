import json
from operator import itemgetter

ruta = ""


def productos_menos_vendidos(fecha_incio, fecha_fin):
    
    try:
        with open(ruta + "ranking_productos.json", "r") as productos:
            lista_productos = json.load(productos)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontraros productos")
        return
    
    productos_por_fecha = []
    for articulos in lista_productos:
        if articulos["Fecha"] >= fecha_incio and articulos["Fecha"] <= fecha_fin:
            productos_por_fecha.append(articulos)
    if not productos_por_fecha:
        print(f"No hay ventas registradas entre el {fecha_incio} hasta el {fecha_fin}")
        return
    
    productos_por_fecha.sort(key=itemgetter("cantidad_vendida"))
    
    print("Este es el producto mas vendido")
    print(f"{productos_por_fecha[-1]}")
    
    try:
        with open(ruta + "menos_vendidos.json", "w") as mas_vendidos:
            json.dump(productos_por_fecha[-1], mas_vendidos, indent=4)
    except Exception:
        print("Error al guardar el reporte")