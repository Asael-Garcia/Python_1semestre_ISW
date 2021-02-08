print ("Bienvenido a la calculadora de Alumnos aprobados o no")
continuar = "s"
while continuar == "s":
        primero=float(input("Ahora necesito que me des la calificacion del primer parcial: \n"))
        parcial=float(input("Ahora dame la calificacion del segundo parcial: \n"))
        promedio = ((primero + parcial)/2)
        if promedio >= 6:
                print ("El alumno afortunadamente esta aprobado con un calificacion de:", promedio)
        else:
                print ("Por desgracia el alumno no aprobo y tiene  una calificacion de: ", promedio)
        continuar=input("Deseas volver a realizar el calculo de otra calificacion (s/n): ")
       
    
