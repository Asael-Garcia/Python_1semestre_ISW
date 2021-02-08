import os
def mostrar_lista(alumnos):
    print ("Lista de estudiantes")
    contador = 1
    for estudiante in alumnos:
        print (contador,".- ",estudiante,"\n")
        contador += 1
        
def validar():
    bandera = 0
    while (bandera == 0):
        try:
            eleccion = int(input("Elija una opción: "))
            bandera = 1
        except:
            print ("Solamente son los números son váidos")
            bandera = 0
    return eleccion

estudiantes = []
opciones = ("1.- Registrar estudiante", "2.- Lista de estudiantes","3.- Eliminar primero de la lista", "4.- Eliminar último de la lista", "5.- Eliminar estudiante por posición", "6.- Eliminar estudiante por nombre", "7.- Lista ordenada", "8.- Salir")
eleccion = 1
while (eleccion != 8):
    os.system("cls")
    print ("Control escolar\n")

    for opcion in opciones:
        print (opcion)

    eleccion = validar()
    os.system("cls")
    if eleccion == 1:
        print ("Registro de estudiante")
        estudiantes.append(input("Nombre del estudiante: ").upper())
        print ("Estudiante registrado")
        
    elif eleccion == 2:
         mostrar_lista(estudiantes)
            
    elif eleccion == 3:
        print ("Eliminar el primer estudiante\n")
        estudiantes.pop(0)
        print ("Estudiante eliminado")
        
    elif eleccion == 4:
        print ("Eliminar último estudiante\n")
        estudiantes.pop()
        print ("Estudiante eliminado")
      
    elif eleccion == 5:
        print ("Eliminar estudiante por posición\n")
        mostrar_lista(estudiantes)
        print ("\nIndica la posición del estudiante a eliminar: (0..",len(estudiantes) - 1,") ")
        posicion = validar() -1
        if (estudiantes.pop(posicion)):
            print ("Estudiante eliminado")
        else:
            print ("La posicion indicada no existe en la lista")
        
    elif eleccion == 6:
        print ("Eliminar estudiante por nombre\n")
        mostrar_lista(estudiantes)
        nombre = input("\nIndica el nombre del estudiante a eliminar: ").upper()
        try:
            estudiantes.remove(nombre)
            print ("\nEstudiante eliminado\n")
        except:
            print ("\nEl estudiante indicado no existe en la lista\n")
	
    elif eleccion == 7:
        print ("Lista de estudiantes ordenada")
        contador = 1
        estudiantes.sort()
        for estudiante in estudiantes:
            print (contador,".- ",estudiante,"\n")
            contador += 1
	
    elif eleccion == 8:
        print ("Hasta luego.")
    else:
        print ("Elija una opción válida (1-5)")
    
    input("Presiona ENTER para continuar ...")
