import numpy as np
print("¡ Bienvenido a Auto Seguro” !\n")
lista_auto=[]
def mostrar_opciones(): #creacion de menu principal
    global op
    op=""
    while(op != "1" and op != "2" and op != "3" and op != "4"):
        op= input("Ingrese una opcion:\n \n1. Guardar auto \n2. Buscar auto \n3. Imprimir certificado \n4. Salir \n\nOpcion: ")
        print("") #salto
    else:
        if op=="1":
            grabar_auto()
    """    elif op=="2":
            buscar_auto()
        elif op=="3": #
            imprimir_certificado()
        elif op=="4":
            print("\n¡ Hasta pronto !\n")
"""
def grabar_auto(): 
    global patente
    global auto
    while(True): 
        try:
            marca=""
            while len(marca)<2 or len(marca)>15:
                marca= input("Ingrese marca del vehiculo: ") 
                if len(marca)<2 or len(marca)>15:
                    print("Error, marca del vehiculo debe conter mínimo 2 caracteres, máximo 15 ") 
                else:
                    print("marca ingresada correctamente")
            patente= input("Ingrese patente del vehiculo: ")
            while len(patente)!=6:
                print("Patente debe tener 6")
                patente= input("Ingrese nuevamente: ")
            else:
                print("patente ingresada correctamente")
            Nombre_dueno= input("Ingrese nombre del dueño: ") 
            Tipo= input("Ingrese tipo del vehiculo: ") 
        except:
            print("Favor vuelva a intentar")      
        break   
    while(True):
        try:
            Valor=0
            while Valor<5000000:
                Valor= int(input("Ingrese valor del vehiculo: "))
                print("Monto insuficiente, favor vuelva a ingresar")
            else:
                break
        except:
            print("Error de ingreso, favor vuelva a intentar")    
    print("\nDatos ingresados correctamente\n")
    print("")
    auto={"Dueno":Nombre_dueno,"Tipo":Tipo,"marca":marca,"patente":patente,"Valor":Valor}
    lista_auto.append(auto.copy())
    print(lista_auto)
    for datos in auto:
        print(datos,":",auto[datos])
    

def buscar_auto():   
    index=0
    while(True): 
        try:
            patente_busqueda= input("Ingrese patente del auto que desea buscar: ")
            for busqueda in lista_auto:
                index=index+1
                if patente==busqueda["patente"]: 
                    for datos in auto:
                        print(datos,":",auto[datos])
                
        except:
            print("Error de ingreso, favor vuelva a intentar")   
mostrar_opciones()