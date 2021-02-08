import os


valor_general=[]
ventas=[[]]
contador=0
bandera=0
while bandera!=1:
    print("Dame el precio del producto: ")
    precio=int(input())
    if precio>0:
        ventas[contador].append(precio)
        print("____Precio registrado____")
        print (ventas)
        bandera=0
    elif precio<1:
        valor_nuevo=str(precio)
        print("\n")
        print(valor_nuevo)
        print (type(valor_nuevo))
        if valor_nuevo=="0":
            valor_clientes=sum(ventas[contador])
            valor_general.append(valor_clientes)
            print(valor_general)
            print("Sumatoria de los productos de este cliente: ", valor_clientes)
            ventas.append([])
            print ("_____Se ha creado una nueva lista:________")
            bandera=0
            contador=contador+1
        elif valor_nuevo=="00":
            print("Sumatoria general de todos los productos", sum(valor_general))
            bandera=1
        else:
            print("Error")
    