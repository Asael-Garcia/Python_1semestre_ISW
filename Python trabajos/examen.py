#examene del segundo parcial
def rellenando():
    ventas=[[]]
    bandera_principal=True
    longitud=1
    contador=0
    while bandera_principal:
        for i in range (0,longitud):
            bandera="0"
            precio, respuesta=meter_cosas(bandera,contador,ventas)
            if precio==0:
                ventas.append([])
                print ("La sumatoria de lo que compro este clientes es", sum(ventas[contador]))
                print("Pasaremos al siguiente cliente")
                contador=contador+1
                bandera_principal=True
            if respuesta=="00":
                print ("La sumatoria de todas los productos seria de: ", sum(*ventas))
                break
            else:
                continue

def meter_cosas(bandera,contador,ventas):
    while bandera!="00":
        print("Para el cliente numero ",(contador))
        print("Dame el precio del producto: ",)
        precio=float(input())
        ventas[contador].append(precio)
        print (ventas)
        if precio==0:
            bandera="00"
        else:
            print("¿Deseas seguir añidiendo mas productos? 0 para si 00 para no")
            respuesta=str(input())
            bandera="00"
    return precio,respuesta


rellenando()