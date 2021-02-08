#PRACTICA CON MIGUE 26/11/2020
import os
asistentes=[]#arreglo vacio para ingresar los asistentes
continuar="s"
while continuar=="s":
    os.system ("cls")
    asistentes.append(input("Indique el nombre del invitado: ").title())#el .capitalize() sirve para convertir la primera letra del string en mayuscula
                                                               #.title() este sirve para poner la primera letra en mayusucla de mas de una palabra ejemplo: alma serrano => Alma Serrano
    continuar=input("Desea agregar otro nombre: ").lower()#para hacer minuscula la respuesta
                                                #.upper() para hacer mayuscula
#primera forma de hacer la lista
os.system("cls")
print("Lista de asistentes: ")
for i in asistentes:#aqui digo que para i en el arreglo asistentes
    print (i) #imprimiria i, incia en 0 automaticamente, asi me imprime todo lo que hay en el arreglo

#otra forma de hacer las listas
print ("\nOtra lista○\n")
for j in range (0,len(asistentes)): #aqui de indica que para j en el rango de 0 a la longitud (len) del arreglo asistentes
    print (asistentes[j]) #me va a imprimir el arreglo asistentes en la posicion j