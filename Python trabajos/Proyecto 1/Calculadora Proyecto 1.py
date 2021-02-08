print ("Bienvenido a tu calculadora")
continuar="s"
while continuar == "s":
    print ("Selecciona en el menu que operacion deceas hacer: \n")
    print ("Suma (1)")
    print  ("Resta (2)")
    print ("Multiplicacion (3)")
    print ("Division (4)")
    numerito =input("Dame tu respuesta rey: ")
    if numerito=='1':
        numero1=float(input("Necesito que me des el primero numero que desees sumar: "))
        numero2=float(input("Ahora necesito que me des el segundo numero rey: "))
        resultado = numero1 + numero2
        print ("El resultado de tu operacion es de: ", resultado)
    elif numerito=='2':
        numero1=float(input("Necesito que me des el numero al que quieres restarle "))
        numero2=float(input("Ahora necesito el numero que vas a restar: "))
        resta  = numero1 - numero2
        print ("El resultado de la operacion que estas buscando es de: ", resta)
    elif numerito=='3':
        numero1=float(input("Necesito que me des el numero que quiera multiplicar: "))
        numero2=float(input("Ahora necestio el segundo numero: "))
        multiplicacion = numero1 * numero2
        print ("El resultado que estas buscando es de: ", multiplicacion)
    elif numerito=='4':
        numero1=float(input("Necesito que me des el numero que quieras dividir: "))
        numero2=float(input("Ahora necesito que me des el numero divisor: "))
        division = numero1 / numero2
        print ("El resultado que estas buscando es de: ", division)
    else:
        print ("Syntax Error")
    continuar=input("Deseas realizar algun otro calculo rey (s/n): ")
 
    
