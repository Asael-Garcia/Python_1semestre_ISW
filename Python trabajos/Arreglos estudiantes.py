estudiantes =[]
opciones = ["1.- Registrar estudiante", "2.- Lista de estudiantes", "3.- Eleminar primer estudiante", "4.- Eliminar ultimo de la lista", "5.- Eleminar estudiante por pocision", "6.- Eleminar estudiante por nombre", "7.- Lista ordenada", "8.- Salir"]
eleccion =1
while (eleccion !=0):
    print ("Control escolar\n")
    for opcion in opciones:
        print (opcion)
    print ("Eleja una opcion")
    eleccion=int(input())
    if eleccion ==1:
        print ("Registro del estudiante")
        estudiantes.append(input("Nombre del estudiante: ").upper())
    elif eleccion==2:
    elif eleccion==3:
    elif eleccion==4:
    elif eleccion==5:
    elif eleccion==6:
    elif eleccion==7:
    elif eleccion==8:
    else:


    
    
