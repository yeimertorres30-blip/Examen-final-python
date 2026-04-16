from crearProductos import *
from crearMesas import *
from crearClientes import *
from generarFactura import *
from generarReporte import *


def menu():
    
        
        decoracion = "=" * 50
        opcion = 0
        
        
        
        while opcion != 6:
                
            try:
            
                print(decoracion)
                print("Bienvenido al restaurante ACME")
                print("            MENU              ")
                print("1. Crear Productos")
                print("2. Crear Mesas")
                print("3. Crear Clientes")
                print("4. Generar Factura")
                print("5. Generar Reporte de Ventas")
                print("6. Salir")
                opcion = int(input("Ingrese una opcion : "))
            
            
                print("==============================")
                match opcion:
                    case 1:
                        crearProductos()
                    case 2:
                        crearMesas()
                    case 3:
                        crearClientes()
                    case 4:
                        generarFactura()
                    case 5:
                        generarReporte()
                    case 6:
                        print("Saliendo......")
                    case _:
                        print("Opcion invalida")
                        
            except Exception as e:
                print("A ocurrrido un error :(")
                print(f"{type(e).__name__} - {e}")
            
    