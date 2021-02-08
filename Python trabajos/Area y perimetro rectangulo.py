continuar = "s"
while (continuar == "s") :
    print ("Bienvenido a tu calculadora de areas y/o perimetros de rectangulos")
    base = float(input("Indica la medida de la base: "))
    altura = float(input("Indica la medida de la altura: "))
    respuesta = input("En caso de que quieras calcular el área del rectangulo preciona 1, en caso del perimetro presiona 2: ")
    if respuesta == "1" :
        area=base * altura
        print ("El area que estas buscando es de: ", area , " cm2")
    else:
        perimetro = base + base + altura + altura
        print ("El perimetro que estas buscando es de: ", perimetro , " cm")
    continuar=input("Desea volver a realizar otro calculo, en caso de que si precione la tecla s, de lo contrario presione cualquier otra letra: ") 

