import json
import csv


def generarReporte():
    
    ruta = ""
    decoracion = "=" * 60
    
    encabezado = ["Mesa", "Total productos", "Subtotal bruto", "Subtotal Iva" , "Total General"]
    
    total_venta_bruta = 0
    total_iva = 0
    total_ventas = 0
    lista_ventas = []
    
    print(decoracion)
    print("REPORTE")
    fecha_reporte = input("Ingrese la fecha del reporte en dd/mm/aa : ")
    
    try:
        with open(ruta + "respaldo_reporte.json", "r") as reporte:
            datos_reporte = json.load(reporte)
            
            
        print(f"Resumen de ventas del {fecha_reporte}")
        print(decoracion)
        
        for ventas in datos_reporte:
            if ventas["fecha"] == fecha_reporte:
                
                mesa = ventas["mesa"]
                cantidad = ventas["total productos"]
                venta_bruto = ventas["subtotal_bruto"]
                iva = ventas["subtotal_iva"]
                total = ventas["subtotal"]
                
                print(decoracion)
                print(f"Mesa : {mesa} Cantidad : {cantidad}")
                print(f"venta_bruto : {venta_bruto} iva : {iva}")
                print(f"Total : {total}")
                print(decoracion)
                
                total_venta_bruta += venta_bruto
                total_iva += iva
                total_ventas += total
                lista_ventas.append([mesa, cantidad, venta_bruto, iva, total])
                
        print(decoracion)
        print(f"Total venta bruta: ${total_venta_bruta}")
        print(f"Total IVA : ${total_iva}")
        print(f"Total de ventas : {total_ventas}")
        print(decoracion)
        
        if len(lista_ventas) > 0:
            print("¿Desea imprimir el reporte en un archivo CSV?")
            print("1. Si")
            print("2. No")
            opcion = int(input("Elija una opción: "))
            
            if opcion == 1:
                nombre_csv = f"Reporte_ventas_{fecha_reporte.replace('/', '-')}.csv"
                with open(ruta + nombre_csv, "w", newline="") as archivo_csv:
                    escribir = csv.writer(archivo_csv)
                    
                    escribir.writerow(encabezado)
                    escribir.writerows(lista_ventas)
                    escribir.writerow([])
                    escribir.writerow(["Totales", "", total_venta_bruta, total_iva, total_ventas])
                print("Archivo generado con exito")
                
        else:
            print("No se encontraron ventas para la fecha ingresada")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: no hay datos de ventas registrados todavia para esa fecha.")
        
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")
