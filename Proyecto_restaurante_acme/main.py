from crearProductos import *
from crearMesas import *
from crearClientes import *
from generarFactura import *
from generarReporte import *
from ranking_productos import *
   
decoracion = "=" * 50
opcion = 0
               
while opcion != 7:  
                 
    try:   
        print(decoracion)
        print("Bienvenido al restaurante ACME")
        print("            MENU              ")
        print("1. Crear Productos")
        print("2. Crear Mesas")
        print("3. Crear Clientes")
        print("4. Generar Factura")
        print("5. Generar Reporte de Ventas")
        print("6. Ranking de productos más vendidos")
        print("7. Salir")
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
                fecha_inicio = input("Ingrese la fecha de inicio en formato dd/mm/aa : ")
                fecha_fin = input("Ingrese la fecha de fin en formato dd/mm/aa : ")
                productos_menos_vendidos(fecha_inicio, fecha_fin)
            case 7:
                print("Saliendo.....")
            case _:
                print("Opcion invalida")
                        
    except Exception as e:
        print("A ocurrrido un error :(")
        print(f"{type(e).__name__} - {e}")
#importaciones
import menu
        
#llamar funciones
menu.menu()
