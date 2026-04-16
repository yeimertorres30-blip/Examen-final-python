
import json



def crearProductos():
   
    decoracion = "=" * 50
 
    print(decoracion)
    print("Modulo de ingresar producto")
    
    try:
        with open("productos.json", "r") as productos:
                
            lista_productos = json.load(productos)
                
    except (FileNotFoundError, json.JSONDecodeError):
            
        lista_productos = []
    
    
    
    #no dejar que se repitan los codigos
    
    try:
        while True:
            try:
                codigo = int(input("Ingrese el codigo del producto: "))
                existe = False
                for producto in lista_productos:
                    if producto["codigo"] == codigo:
                        existe = True
                        break
                if existe:
                    print("Error, ese codigo ya existe")
                else:
                    break
            except ValueError:
                print("Por favor ingrese solo numeros")
                
        while True:       
            nombre = input("Ingrese el nombre del producto: ")
            if nombre.replace(" ", "").isalpha():
                break
            else:
                print("Ingrese solo letras")
                
        while True:    
            try:    
                valor_unitario = int(input("Ingrese el valor unitario de ese producto: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros") 
                
        while True:
            try:
                iva = int(input("Ingrese el IVA de este producto: "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros : ")
            
        
        
   
    
        datos_producto = {
            "codigo" : codigo,
            "Nombre" : nombre ,
            "Valor Unitario" : valor_unitario,
            "Iva" : iva
        }
        
            
        lista_productos.append(datos_producto)
            
        
        with open("productos.json", "w") as archivo:
            json.dump(lista_productos, archivo, indent=4)
        
        print("Producto guardado exitosamente")
            
    except ValueError:
        print("Por favor ingrese algo valido")
        
    print(decoracion)