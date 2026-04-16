from datetime import datetime
import json

decoracion = "=" * 50

def generarFactura():
    
    print(decoracion)
    
    #Ya tenemos los datos de la mesa
    print("MESAS DISPONIBLES")
    
    with open("Mesas.json" , "r") as mesas:
        datos = json.load(mesas)
        
        #mejorar la visualisacion
        
        for mesa in datos:
            codigo = mesa.get("Codigo", "N/A")
            nombre = mesa.get("Nombre", "N/A")
            puestos = mesa.get("Puestos", "0")
            
            print(f"Mesa: {codigo} con {puestos} puesto -> {nombre}" )
    
    codigo_mesa = int(input("Ingrese el codigo de la mesa a atender: "))
        
    datos_mesa = buscar_datos_jason("Mesas.json", "Codigo", codigo_mesa)
    
    if not datos_mesa:
        print("Mesa no encontrada.")
        print("No se puede inciar facturación")
        return
    
    id_cliente = int(input("Ingrese el numero de documento del cliente: "))
    datos_cliente = buscar_datos_jason("Clientes.json", "Identificacion", id_cliente)
    
    if not datos_cliente:
        print("Cliente no encontrado")
        print("No se puede inciar la facturacion")
        return
    
    
    #ya tenemos la fecha actual formateada
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%d/%m/%y")
    
    
    if datos_mesa and datos_cliente:
        print(f"Generando factura para {datos_cliente["Nombre"]} con la mesa {datos_mesa["Nombre"]}")
        print("Lista de productos")
        with open("productos.json", "r") as productos:
            lista_productos = json.load(productos)
            
            for items in lista_productos:
                print(f"{items["codigo"]} : {items["Nombre"]} ${items["Valor Unitario"]}")
                
        #El usuario añade los productos por medio del codigo
        
        continuar = 1
        productos_a_facturar = {}
        
        while continuar == 1:
              
            productos_elegidos = int(input("Ingrese el codigo del producto que desea: "))
            producto_encontrado = buscar_datos_jason("productos.json", "codigo", productos_elegidos)
            
            if producto_encontrado:
                cantidad = int(input(f"Ingrese la cantidad que desea de {producto_encontrado["Nombre"]} : "))
                
                datos_producto = { 
                    "Nombre": producto_encontrado["Nombre"], 
                    "Valor Unitario": producto_encontrado["Valor Unitario"], 
                    "Iva": producto_encontrado["Iva"],
                    "Cantidad" : cantidad
                }
                
                productos_a_facturar[productos_elegidos] = datos_producto
            else:
                print("Producto no encontrado")
                
            while (True):
                
                print("¿Desea agregar otro producto?")
                print("1. SI")
                print("2. NO")
                continuar = int(input("Ingrese la opcion: "))
                
                if continuar == 1 or continuar == 2:
                    break
                else:
                    print("Opcion invalida")

        if continuar == 2:
            #se genera la factura
            generarfactura(datos_mesa, datos_cliente, fecha_formateada, productos_a_facturar)
            
        if continuar != 1 and continuar != 2:
            #debemos combatir este error no dejar que haga error si el usuairo no elije ninguna de las 2
            print("Opción invalida")
        
    
    print(decoracion)
    
    
    
def buscar_datos_jason(nombre_archivo, clave, valor):
    try:
        with open(nombre_archivo, "r") as archivo:
            datos_archivo = json.load(archivo)
            for datos in datos_archivo:
                if datos.get(clave) == valor:
                    return datos
        
    except Exception:
        print("Ha ocurrido un error :(")
        
def generarfactura(mesa, cliente, fecha, productos):
    
    print(decoracion)
    print("FACTURA")
    print(f"Cliente : {cliente["Nombre"]}")
    print(f"Mesa: {mesa["Codigo"]} -> {mesa["Nombre"]} de {mesa["Puestos"]} puestos")
    print(f"Fecha : {fecha}")
    
    total_a_pagar = 0
    
    print(f"Productos solicitados")
    print(decoracion)
    for codigo, info_producto in productos.items():
        
        subtotal = ((int(info_producto["Valor Unitario"]) + int(info_producto["Iva"])) * info_producto["Cantidad"])
        
        print(f"{info_producto["Nombre"]} : {info_producto["Cantidad"]} unidades | Total = {subtotal}")
        
        total_a_pagar += subtotal
        
    print(decoracion)
    
    
   
    print(f"Total a pagar : {total_a_pagar}")
    
    print(decoracion)
    
    print("¿Desea guardar la factura?")
    print("1. Si")
    print("2. No")
    guardar_factura = int(input("Ingrese una opción: "))
    
    total_a_paga_txt = 0
    subtotal_bruto = 0
    subtotal_iva = 0
    total_productos = 0
    
    for codigo, info_producto in productos.items():
        cantidad = info_producto["Cantidad"]
        valor_unidad = int(info_producto["Valor Unitario"])
        iva = int(info_producto["Iva"])
        
        subtotal_item = (valor_unidad + iva) * cantidad
        
        
        total_a_paga_txt += subtotal_item
        subtotal_bruto += valor_unidad * cantidad
        subtotal_iva += iva * cantidad
        total_productos += cantidad
    
    if guardar_factura == 1:
        
        nombre_archivo = f"Factura para {cliente["Nombre"]}.txt"
        #Guardarlo como archivo txt
        with open(nombre_archivo, "w") as factura:
            
            factura.write(decoracion + "\n")
            factura.write("FACTURA DE VENTA \n")
            factura.write(decoracion + "\n")
            factura.write(f"Fecha : {fecha}\n")
            factura.write(f"Cliente : {cliente['Nombre']} Nº {cliente['Identificacion']}\n")
            factura.write(f"Numero de contacto : {cliente['Telefono']}\n")
            factura.write(f"Email : {cliente['Email']}\n")
            factura.write(f"Mesa : {mesa['Nombre']} Nº {mesa['Codigo']}\n")
            factura.write(decoracion + "\n")
            factura.write("PRODUCTOS\n")
            
            for codigo, info_producto in productos.items():
        
                subtotal = ((int(info_producto["Valor Unitario"]) + int(info_producto["Iva"])) * info_producto["Cantidad"])
                
                factura.write(f"{info_producto["Nombre"]} : {info_producto["Cantidad"]} unidades \n valor unitario : {info_producto["Valor Unitario"]}\n Iva : {info_producto["Iva"]} \n Total = {subtotal}\n")
                
                
            factura.write(f"Total a pagar = {total_a_paga_txt}\n")
            factura.write(decoracion + "\n")
            generar_archivo_para_reporte(mesa["Codigo"], total_productos, subtotal_bruto, subtotal_iva, total_a_paga_txt, fecha, imprimio=True)
        
    if guardar_factura == 2:
        #Imprimir subtotal de nuevo
        print("Ok haz elegido no guardar la factura")
        print(f"El total a pagar es: {total_a_pagar}")
        
        generar_archivo_para_reporte(mesa["Codigo"], total_productos, subtotal_bruto, subtotal_iva, total_a_paga_txt, fecha, imprimio=False)
    
    
    
def generar_archivo_para_reporte(mesa, total_productos, subtotal_bruto, subtotal_iva, subtotal, fecha, imprimio):
    
    print(decoracion)
    
    
    imprimido_o_no = ""
    
    if imprimio:
        imprimido_o_no = "Se guardo la factura"
    else:
        imprimido_o_no = "No se guardo la factura"
    
    molde_reporte = {
        "fecha" : fecha,
        "mesa" : mesa,
        "imprimio" : imprimido_o_no,
        "total productos" : total_productos,
        "subtotal_bruto" : subtotal_bruto,
        "subtotal_iva" : subtotal_iva,
        "subtotal" : subtotal,
    }
    
    try:
        with open("respaldo_reporte.json", "r") as clientes:
                lista_datos = json.load(clientes)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_datos = []
    
    
    lista_datos.append(molde_reporte)
    
    with open("respaldo_reporte.json", "w") as archivo:
        
        json.dump(lista_datos, archivo, indent=4)
            
    
    print(decoracion)
    
    
    