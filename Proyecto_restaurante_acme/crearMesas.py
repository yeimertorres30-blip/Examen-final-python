import json


def crearMesas():
    decoracion = "=" * 50
    print(decoracion)
    print("Modulo de crear mesas")
    
    try: 
        with open("Mesas.json", "r") as archivo:
            lista_mesas = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
            lista_mesas = []
    
    try:
        while True:
            try:
                codigo = int(input("Ingrese el codigo de la mesa : "))
                existe = False
                for mesa in lista_mesas:
                    if mesa["Codigo"] == codigo:
                        existe = True
                        break
                if existe:
                    print("Este codigo ya existe")
                else:
                    break
            except ValueError:
                print("Por favor ingrese solo numeros")
        
        
        while True:
            nombre = input("Ingrese el nombre de la mesa : ")
            if nombre.replace(" ", "").isalpha():
                break
            else:
                print("Ingrese solo letras")
        
        
        while True:
            try:
                puestos = int(input("¿cuantos puestos tiene esta mesa? : "))
                break
            except ValueError:
                print("Por favor ingrese solo numeros")
        
        
        
        datos_mesas = {
            "Codigo" : codigo,
            "Nombre" : nombre,
            "Puestos" : puestos
        }
        
            
        lista_mesas.append(datos_mesas)
        
        with open("Mesas.json", "w") as archivo:
                json.dump(lista_mesas, archivo, indent=4)
                
        print("Mesa guardada")
        
    except ValueError:
        print("Ingrese un dato valido")
    

        
    print(decoracion)   