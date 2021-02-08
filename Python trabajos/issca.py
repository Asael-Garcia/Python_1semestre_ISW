salidas=[[]]
salida=0
precio=None
def funka():
    salidas[salida].append(int(precio))
perse=0
while perse==0:
    precio=input("Ingrese el precio: ")
    if precio=="0":
        print("El total de su compra es: ", sum(salidas[salida]))
        salidas.append([])
        salida+=1
    elif precio=="00":
        total=0
        for salida in salidas:
            total+=sum(salida)
        print(fo"El total al corte es: {total}")
        break
    else:
        funka()