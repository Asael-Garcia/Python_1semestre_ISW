#variables globales


#una variable para pedir nombre
def pedir_nombre():
    global nombre #determino la variable como una variable global para poder usarla fuera de esta mism variable
    global edad #determino la variable como una variable global para poder usarla fuera de esta mism variable
    nombre= input("¿cual es tu nombre: ")
    edad=int(input("Ahora dame tu edad: "))

def saludar():
    print ("Hola ",nombre," tu edad es: ", edad, "años")#mando a llamar la variable nombre que es global
                                            #la edad la hago string 


#el global me sirve como un return, pero de esta manera puedo usar la variable que marco en todo el programa
#de esta manera se pueden hacer varias variables globales dentro de una funcion para poder usarlas en otra sin usar un return
pedir_nombre()
saludar()




#OTRA FORMA DE HACER LAS VARIABLES GLOBALES