import os
def imprimir_numeros ():
    for i in range (1,11):#establezco mi funcion donde imprimo los numero del 1 al 10
        print (i)

imprimir_numeros()#mando a llamar mis numero, como no tiene parametros
#no pongo nada en los parentesis



#DEFINO ALGUNAS DE MIS VARIABLES
global dinerito

print ("\n")

print ("SEGUNDO EJERCISIO")


def menu():
    print ("1. Dolar")
    print ("2. Dolar Canadiense")
    print ("3. Euro")
    print ("4. Libra Esterlina")
    print ("5. Centenario")
    print ("¿Cuanto tienes en pesos mexicanos?")
    global pesos
    pesos=float(input())
    print ("¿Que tipo de cambio deseas realizar?: ")
    global cambio
    cambio=int(input())
    #evaluendo el tipo de cambio
    if cambio==1:
        dolares()#Llamo a la funcion dolares
    elif cambio==2:
        dolar_canadiense()#llamo a la funcion de dolar canadience
    elif cambio==3:
        euro()#Llamo a la funcion del euro
    elif cambio==4:
        libra_esterlina()
    elif cambio==5:
        centenario()
    else:
        print ("Elije una opcion disponible")
        
#defino la funcion para el calculo de dolares
def dolares():
    print ("¿Cual es el peso del dolar el dia de hoy?")
    global precioDolar
    precioDolar=float(input())
    dinerito=pesos/precioDolar
    print ("El cambio de tu moneda es de: ", dinerito, " dolares")




#defino la funcion para el calculo de dolares canadienses
def dolar_canadiense():
    print ("¿Cual es el valor del dolar canadiense al dia de hoy?")
    global precioCanadiense
    precioCanadiense=float(input())
    dinerito=pesos/precioCanadiense
    print("El cambio de tu moneda es de: ", dinerito, "dolares canadienses")


#defino la funcion para el calculo del euro
def euro():
    print ("¿Cual es el valor del euro en pesos mexicanos al dia de hoy?")
    global precioEuro
    precioEuro=float(input())
    dinerito=pesos/precioEuro
    print ("El cambio de tu moneda es de: ", dinerito, " euros")


#defino la funcion para la libra esterlina
def libra_esterlina():
    print ("¿Cual es el valor de la libra esterlina en pesos mexicanos al dia de hoy?")
    global precioLibra
    precioLibra=float(input())
    dinerito=pesos/precioLibra
    print ("El cambio de tu moneda es de: ", dinerito, " libras esterlinas")



#defino la funcion para el centenario
def centenario():
    print ("¿Cual es el valor del centenario en pesos mexicanos al dia de hoy?")
    global precioCentenario
    precioCentenario=float(input())
    dinerito=pesos/precioCentenario
    print ("El cambio de tu moneda es de: ", dinerito, " centenarios")


#Llamando a la funcion menu e inicio un ciclo while para poder realizar todo
continuar=("s")
while continuar=="s":
    menu()
    print ("\n")
    print ("Deseas continuar? s/n: ")
    continuar=str(input())

    
