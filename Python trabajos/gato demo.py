import os



#codifo final


tablero=[["-","-","-"],["-","-","-"],["-","-","-"]]
turno=0
#muestro mi tablero
def mostrar_tablero(tablero):
    for i in range(0,3):
        for j in range (0,3):
            print(tablero[i][j], end=" ")
        print ("\n")



#DETERMINO MIS JUGADORES
def determinar_jugador():
    global jugador1
    global jugador2
    global jugador_auxiliar
    bandera_jugador=False
    while bandera_jugador==False:
        print ("___Determinar jugador____")
        print ("Jugador 1, por favor decide que quieres ser (X o O): ")
        jugador1=str(input()).upper()
        if jugador1=="X":
            print("Jugador 1, tu pieza es X, jugador dos tu pieza es O")
            jugador_auxiliar=jugador1
            jugador2="O"
            bandera_jugador=True
        elif jugador1=="O":
            print("Jugador 1, tu pieza es O, jugador dos tu pieza es X")
            jugador_auxiliar=jugador1
            jugador2="X"
            bandera_jugador=True
        else:
            print("Opcion invalida, por favor seleccione una de las opciones disponibles")
            bandera_jugador=False



#CAMBIAR DE JUGADOR
def cambiar_jugador():
    global turno
    global jugador1
    global jugador2
    global jugador_auxiliar


    if (turno!=0):
        if jugafor_auxiliar==jugador1:
            jugdor_auxiliar==jugador2
        else:
            jugador_auxiliar=jugador1
        turno=turno+1#para marcar las vueltas o turnos que llevo
    else:
        turno=turno+1#para marcar que voy a llevar mi primera vuelta


#DEFINO LOS MOVIMIENTOS
def movimiento(tablero):
    global jugador_auxilar
    cambiar_jugador()

    bandera=True

    while bandera:
        try:
            print ("Ingresa su cordena, empezando por la fila\n: ")
            fila=int(input())
            print("Ingresa su cordenada, ahora por la columna: ")
            columna=int(input())
            if fila>=0 and fila<=2 and columna>=0 and columna<=2:
                if tablero[fila][columna]=="-":
                    bandera=False
                    tablero[fila][columna]=jugador_auxiliar
                    mostrar_tablero()
                else:
                    print("Esta casilla esta ocupada")
            else:
                print ("Solo se aceptan numeros del 0-2")
        except:
            print("Solo se aceptan numero")

    
determinar_jugador()
movimiento(tablero)







#TRASPASO DE CODIGO
#codigo principal

#pedir_jugada()

#GATO FINAL

tablero=[["-","-","-"],["-","-","-"],["-","-","-"]]

#muestro mi tablero
def mostrar_tablero(tablero):
    for i in range(0,3):
        for j in range (0,3):
            print(tablero[i][j], end=" ")
        print ("\n")
            
#determino los jugadores
def determinar_jugador():
    bandera_jugador=False
    global jugador1
    global jugador2
    global jugador_auxiliar
    while bandera_jugador==False:
        print ("Jugador uno, selecciona tu figura (X u O):")
        jugador_auxiliar=str(input()).upper()
        if jugador_auxiliar=="X":
            jugador1="X"
            jugador2="O"
            print ("Jugador 1, tu fica es: ", jugador1)
            print ("Jugador 2, tu fica es: ", jugador2)
            bandera_jugador=True
            movimiento(jugador1,jugador2,jugador_auxiliar,tablero)
        elif jugador_auxiliar=="O":
            jugador1="O"
            jugador2="X"
            print ("Jugador 1, tu ficha es: ", jugador1)
            print ("Jugador 2, tu ficha es: ", jugador2)
            bandera_jugador=True
        else:
            print("Opcion invalida, por favor seleccione una opcion valida")
            bandera_jugador=False
        




#funcion para poder hacer el movimiento deseado
def movimiento(jugador1,jugador2,jugador_auxiliar,tablero):
    flag=0
    print ("____DETERMINAR JUGADA_____")
    while flag<9:
        bandera_movimientoX=False
        bandera_movimientoO=False
        while bandera_movimientoX==False:
            print ("Jugador 1, haz tu movimiento, empezando por la fila, despues por la columna")
            print ("Fila: ")
            fila=int(input())
            print ("Columna:")
            columna=int(input())
            if tablero[fila][columna]=="-":
                print ("Movimiento registrado")
                bandera_movimientoX=True
                tablero[fila][columna]=jugador1
                flag=flag+1
            else: 
                print("La casilla que quieres usar esta ocupada, ingresa otras cordenadas por favor")
                bandera_movimientoX=False
            mostrar_tablero(tablero)
        while bandera_movimientoO==False:
            print ("Jugador 2, haz tu movimiento, empezando por la fila, despues por la columna")
            print ("Fila: ")
            fila=int(input())
            print ("Columna:")
            columna=int(input())
            if tablero[fila][columna]=="-":
                print ("Movimiento registrado")
                bandera_movimientoO=True
                tablero[fila][columna]=jugador2
                flag=flag+1
            else: 
                print("La casilla que quieres usar esta ocupada, ingresa otras cordenadas por favor")
                bandera_movimientoO=False
            mostrar_tablero(tablero)
        
        


#mostrar_tablero(tablero)
determinar_jugador()

