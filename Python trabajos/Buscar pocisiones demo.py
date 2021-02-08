arreglo=[5,10,12,19,20]#arreglo
def contar_jugada(arreglo):
    print ("Dame tu jugada comenzando con el eje x")
    print (arreglo)
    x=int(input())#numero buscado
    try:#try catch para poder buscar el numero que se pidio antes
        posicion=arreglo.index(x)#indico lo que el valor que buscara
        print ("El numero que buscas se encuentra en la pocision: ", posicion+1)#imprimo en que lugar se encuentra ese valor
    except:
        print("Numero no encontrado")

    print ("Ahora dame un numero para añadir a el arreglo")
    numerito=int(input())
    try: 
        arreglo.append(numerito)
        print (arreglo)
    except:
        print("Valor no posible de agregar")


vacio=[]
def guardar_movimiento(vacio):
    for i in range (0,5):#para que haga el ciclo cinco veces
        print("Dame un numero: ")
        numerito=int(input())
        vacio.append(numerito)
        if len(vacio)==5:#si la longitud del arreglo de vacio es igual a 5 termia el programa e imprime el arreglo
            print("Llegaste al limite permitido de 5 datos en el arreglo")
            
            print(vacio)
        else:
            print("Necesitas seguir rellenando los espacios")#si la longitud del arreglo aun no es igual a 5 seguira lanzando este mensaje


unaLista=[]
def ordenamientoBurbuja(unaLista):
    print ("Dame un numero para ingresar: ")
    numerito1=int(input())
    unaLista.append(numerito1)
    print ("Dame un numero para ingresar: ")
    numerito2=int(input())
    unaLista.append(numerito2)
    print ("Dame un numero para ingresar: ")
    numerito3=int(input())
    unaLista.append(numerito3)
    print ("Dame un numero para ingresar: ")
    numerito4=int(input())
    unaLista.append(numerito4)
    print ("Dame un numero para ingresar: ")
    numerito5=int(input())
    unaLista.append(numerito5)
    print ("Dame un numero para ingresar: ")
    numerito6=int(input())
    unaLista.append(numerito6)
    #de aqui en adelante es el ordenamiento burbuja para que me ordene los valores de menor a mayor
    for numPasada in range(len(unaLista)-1,0,-1):#
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


ordenamientoBurbuja(unaLista)
print(unaLista)
