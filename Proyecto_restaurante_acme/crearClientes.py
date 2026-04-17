import json

ruta = ""

def crearClientes():
    decoracion = "=" * 50
    print(decoracion)
    print("Modulo de Crear Clientes")
    
    try:
        with open(ruta + "Clientes.json", "r") as clientes:
            lista_clientes = json.load(clientes)
    except (FileNotFoundError, json.JSONDecodeError):
            lista_clientes = []
            
            
    try:
        while True:
            try:
                
                identificaion = int(input("Ingrese el numero de identificacion: "))
                existe = False
                for cliente in lista_clientes:
                    if cliente["Identificacion"] == identificaion:
                        existe = True
                        break
                if existe:
                    print("Error, ese usuario ya existe")
                else:
                    break
            except ValueError:
                print("Por favor ingrese solo numeros")
                
        while True:
            nombre = input("Ingrese el nombre: ")
            if nombre.replace(" ", "").isalpha():
                break
            else:
                print("Ingrese solo letras")  
                
        while True:
            try:        
                telefono = input("Ingrese el numero de telefono: ")
                break
            except Exception:
                print("A ocurido un error") 
                
        while True:
            try:
                           
                email = input("Ingrese el Email: ")
                break
            except Exception:
                print("A ocurrido un error")
        
    
        datos_cliente = {
            "Identificacion" : identificaion,
            "Nombre" : nombre,
            "Telefono" : telefono,
            "Email" : email
        }
        
            
        lista_clientes.append(datos_cliente)
        
        with open(ruta + "Clientes.json", "w") as archivo:
            json.dump(lista_clientes, archivo, indent=4)
            
        print("Cliente guardado exitosamente")
        
    except ValueError:
        print("Ingrese un dato valido")
        
        
    print(decoracion)
