
tabla=[["-","-","-"],["-","-","-"],["-","-","-"]]



#empieza mi codigo
print("Jugador 1, dime que quieres ser (X ó O): ")
jugador1=str(input())
jugador2=""


#funciones

def inicio():
    global jugador1
    global jugador2
    global jugador3

    jugador1= jugador1.upper()

global bandera

def validacion(movimiento):
    bandera=False
    try:
        movimiento<=2
        movimiento=int
        bandera=True
    except:
        print("Solo se aceptan numeros")
    return bandera


def colocar_pieza():
    print("Ingresa tus cordonadas")
    while validacion(movimiento):
        print ("Jugador 1, ingresa tu cordenada empezando por el eje x")
        filaX=int(input())
        validacion(fialX)


colocar_pieza()