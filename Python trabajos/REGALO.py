#REGALO FALTAN CUMPLIR ALGUNAS CONDICONES DE ENTRADA

import os
#25 pesos por kilometro de distancia cada 100 gramos
print ("---GUANAJUATO SHIPPING COMPANY---")
n=int(input("Dame el numero de regalos a entregar: "))
peso_regalos=[]
distancia=[]
precio_final=[]
os.system("cls")
#calculo del peso
while n>0 and n<1000:

    for i in range(0,n):
        print ("Dame el peso del regalo numero: ", i+1)
        p=int(input())
        peso_regalos.append(p)
        print ("Peso total hasta el momento: ", sum(peso_regalos), " gramos")

    os.system("cls")

    #calculo de la distancia
    for j in range(0,n):
        print ("Dame la distancia de envio del regalo numero: ", j+1)
        d=int(input())
        distancia.append(d)
        print ("La distancia total hasta el momento es de: ", sum(distancia), " km")

    for k in range (0,n):
        peso=peso_regalos[k]/100
        dinero=(peso*0.25)*distancia[k]
        precio_final.append(dinero)
    print ("La sumatoria de todos los envios es de: ", sum(precio_final), " pesos")
    n=-1

