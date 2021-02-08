import random#libreria para sacar un numero random
import os


continuar=str("s")
while continuar=="s":
    print ("Dame tu eleccion para darte un numero random: ")
    eleccion=int(input())
    print ("\n")
    if eleccion==1:
        for i in range(0, 10):
            num=random.randint(0, 10)
            print (num)
    elif eleccion==2:
        numerito=random.randint(1,5)
        print (numerito)
    print ("Deseas
           volver a intentarlo? s/n:")
    continuar=str(input())
    

