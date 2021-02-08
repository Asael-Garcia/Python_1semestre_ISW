import os

#arreglos
tabla=[["-","-","-"],["-","-","-"],["-","-","-"]]


#funciones



#funcion para mostrar el tableero, aqui uso dos fors anidados para poder mostrar mi tablero en forma de matriz 3x3
def mostrar_tablero(tabla):
    for c in range(0,3):
        for f in range (0,3):
            print (tabla[c][f], end=" ")
        print ("\n")
        
#función para validar sólo números, de esta manera no se podran ingresar letras
def validar(mensaje):
    bandera = True
    while bandera:
        try:
            valor = int(input(mensaje))
            bandera = False
        except:
            print ("\nSolamente se admiten números".center(50," "))
    return valor

#funcion CODIGO PRNICIPAL
def pedir_jugada():
    bandera=0#esta bandera me contara las jugadas, y al llegar a nueve jugadas no habra ganador por ende
    bandera_ganador=False#bandera para saber si hay o no ganador, se conecta con la funcion de mostrar ganador
    while bandera<9 and bandera_ganador==False:#un while donde se repetira todo hasta que se hayan hecho 9 jugadas o la bandera ganador sea verdadera
        contadorX=2#este contador sirve para que se sigan pidiendo las cordenadas de X hasta que sean correctas
        while contadorX!=1:#para pedir las cordenadsa de X hasta que sean correctas
            filaX=validar("Jugador X, dame tu jugada, empezando por la fila: ")#valido la fila
            columnaX=validar("Ahora dame en la columna: ")#valido columna
            jugadorX="X"#el valor de X lo asigno a una varibale
            if filaX>=0 and filaX<=2 and columnaX>=0 and columnaX<=2:#para poder saber si la fila y la columna estan dentro de los rangos que hay
                if (tabla[filaX][columnaX]=="-"):#si pasa el if anterior ahora busca que en las filas y columna hata una lina
                    tabla[filaX][columnaX]=jugadorX#si hay una linea, registra el valor del jugador en esa casilla
                    mostrar_tablero(tabla)#muestro el tablero para que se conozca como se van realizando los movimiento
                    contadorX=1#como si se realizo los pasos anteriores el contador de X lo ifualo a 1 para avanze y pida las cordenadas de O
                else:#en caso de que no se cumpla el segundo if, manda el siguiente mensaje de error
                    print("Esta ocupada la casilla que solicitas, vuelve a ingresar las cordenadas")#mensaje de error
                    contadorX=2#el contador de x es dos, para que se vuelva a repetir
            else:#si las filas y columnas no estan dentro del rango pide que las vuelva a ingresar
                print("Opciones invalidas, por favor ingrese valores del 0-2")#las vuelve a pedir
                contadorX=2#contador de x para que se reinicie desde el segundo while y poder volver a ingresar las coordenadas
        bandera=bandera+1#si todo el proceso anteriro se realiza de manera correcta, la bandera de las jugadas aumenta en 1
        bandera_ganador=mostrar_ganador(tabla)#el return que me genera la funcion de mostrar ganador lo almaceno en bandera ganador, para que se pueda cumplir la condicion del primer while
        print("Numero de pocisiones ocupadas: ", bandera)#muestro las jugadas hechas hasta el momento
        if bandera_ganador==True:#aqui pongo este if, ya que por alguna razon el primer while funciona a veces y aveces no, asi que digo que si la bandera de ganador es verdaera
            break#lo que hara este break es romper el ciclo de while, el primero
        else:#en caso de que no se cumlpla eso
            if bandera==9:#si la bandera de movimientos llego a 9 significa que ya no hay espacios disponibles, por lo que termina el juego sin ganador alguno
                print ("Juego terminado, no hay ganador")#no hay ganador
                break#como no hay ganador rompo el ciclo while con este break, el primer while
            #en caso de que no se cumpla alguno de los dos if's anterirores, todo el procedimiento que hice para pedir la jugada con X, lo hago con O
            #repito exactamente lo mismo
            contadorO=2
            while contadorO!=1:
                filaO=validar("Jugador O, dame tu jugada, empezando por la fila: ")
                columnaO=validar("Ahora dame en la columna: ")
                jugadorO="O"
                if filaO>=0 and filaO<=2 and columnaO>=0 and columnaO<=2:
                    if tabla[filaO][columnaO]=="-":
                        tabla[filaO][columnaO]=jugadorO
                        mostrar_tablero(tabla)
                        contadorO=1
                    else:
                        print("Esta ocupada la casilla que solicitas, vuelve a ingresar las cordenadas")
                        contadorO=2
                else:
                    print ("Numeros invalidos, porfavor, vuelva a ingresar las cordenadas")
                    contadorO=2
            #aqui aumento mi bandera de jugadas
            bandera=bandera+1
            bandera_ganador=mostrar_ganador(tabla)#veo si hay un ganador o no
            print("Numero de pocisiones ocupadas: ", bandera)#meustro los movimientos
            continue#este continue, es para que todos los ciclos anteriores prosigan a continuarse y no solo se termine aqui el programa, como decirle que repita el ciclo desde el incio
        break#rompo mi programa
        
        
                


#funcion para determinar ganador, aqui determino a mi ganador insertando todas las maneras posibles de ganar en cordenas, y dependiendo de si hay una X o una O en ese lugar dira quien es el ganador
    #esto gracias al elif que tiene python se me facilito mucho
def mostrar_ganador(tabla):
    bandera_ganador=False#como aun no hay ganador mi bandera ganador es falsa desde el incio
    #para la fila 1
    if tabla[0][0]=="X" and tabla[0][1]=="X" and tabla[0][2]=="X":#condicinante de las cordenadas y el valor que debe estar en ellas
        ganador="¡¡¡Gana el jugador X!!!"#guardo en una varible una mensaje del ganador
        bandera_ganador=True#como si hay ganador mi bandera ganador se vuelve verdadera
        #hago exacamente lo mismo para todas los demas posibles resultados
    elif tabla[0][0]=="O" and tabla[0][1]=="O" and tabla[0][2]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para la fila 2
    elif tabla[1][0]=="X" and tabla[1][1]=="X" and tabla[1][2]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[1][0]=="O" and tabla[1][1]=="O" and tabla[1][2]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para la fila 3
    elif tabla[2][0]=="X" and tabla[2][1]=="X" and tabla[2][2]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[2][0]=="O" and tabla[2][1]=="O" and tabla[2][2]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para columna 1
    elif tabla[0][0]=="X" and tabla[1][0]=="X" and tabla[2][0]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[0][0]=="O" and tabla[1][0]=="O" and tabla[2][0]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para columna 2
    elif tabla[0][1]=="X" and tabla[1][1]=="X" and tabla[2][1]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[0][1]=="O" and tabla[1][1]=="O" and tabla[2][1]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para columna 3
    elif tabla[0][2]=="X" and tabla[1][2]=="X" and tabla[2][2]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[0][2]=="O" and tabla[1][2]=="O" and tabla[2][2]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para diagonal 1\
    elif tabla[0][0]=="X" and tabla[1][1]=="X" and tabla[2][2]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[0][0]=="O" and tabla[1][1]=="O" and tabla[2][2]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    #para diagonla 2/
    elif tabla[0][2]=="X" and tabla[1][1]=="X" and tabla[2][0]=="X":
        ganador="¡¡¡Gana el jugador X!!!"
        bandera_ganador=True
    elif tabla[0][2]=="O" and tabla[1][1]=="O" and tabla[2][0]=="O":
        ganador="¡¡¡Gana el jugador O!!!"
        bandera_ganador=True
    else:
        ganador="Aun no hay ganador..."#Digo que aun no hay ganador alguno
        bandera_ganador=False#si no se cumplio alguna de las condiciones anteriores, la bandera ganador sigue siendo falsa
    print (ganador)#imprimo el ganador
    return bandera_ganador#regreso la bandera jugador, que se conectara en la variable que se encuentra en cel codigo principal, para decidir si se rompe o no el programa


pedir_jugada()#llamo a mi funcion principal
    

  
