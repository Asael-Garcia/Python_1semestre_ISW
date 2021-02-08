continuar = "s"
print ("Bienvenido a tu calculadora de BUN")
while (continuar=="s"):
    urea = float(input("Ahora necesito que me des la canditad de UREA de la sangre: "))
    bun = urea/2.1167
    print ("El nivel de BUN de la urea es de: ", bun, )
    if bun <= 18 :
           print ("Segun tu BUN, el nivel donde te encuentas es NORMAL, asi que no te preucupes tanto")
    else:
        print ("Segun el resultado de tu BUN, el nivel donde te encuentras es ALTO, asi que deberias de preucuparte y empezar a cuidarte más")
    continuar=input("Si quieres seguir calculando mas BUN, preciona la tecla s, de lo contrario presiona cualquier otra tecla: ")
        
        
