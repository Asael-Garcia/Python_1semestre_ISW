continuar="s"
print("Bienvenido a la calculadora de areas y perimetro dde figuaras geometricas")
while (continuar=="s"):
    print("Ahora necestio que selecciones alguna de nuestras opcciones")
    print("Cuadrado (1)")
    print("Rectangulo (2)")
    print("Triangulo (3)")
    print("Circulo (4)")
    respuesta=float(input("Tu respuesta es: "))
    if respuesta==1:
        print("Seleccionaste el cuadrado")
        print("Ahora necesito que me des la medida de cualquier lado")
        lado=float(input())
        area=lado*lado
        perimetro=lado*4
        print("El area y perimetro de figura es de: ")
        print ("AREA: ", area)
        print ("PERIMETRO: ", perimetro)
    elif respuesta ==2:
        print("Selecciconaste rectangulo")
        print("Necesito que me des la medida de la base: ")
        base=float(input())
        print("Ahora dame la medida de la altura: ")
        altura=float(input())
        area= base * altura
        perimetro= base * 2 + altura * 2
        print("El area y perimetro de tu figura es de: ")
        print ("AREA: ", area)
        print ("PERIMETRO: ", perimetro)
    elif respuesta==3:
        print("Seleccionaste triangulo")
        print("Nota; este calculo solo funciona con triangulos equilateros")
        print("Dame la medida de la base")
        base=float(input())
        print("Ahora dame la medida de la altura")
        altura=float(input())
        area=((base * altura)/2)
        perimetro=base*3
        print("El area y perimetro de figura es de: ")
        print("AREA: ", area)
        print("Perimetro: ", perimetro)
    elif respuesta==4:
        print ("Seleccionaste el circulo")
        print ("Dame la medida de el radio")
        radio=float(input())
        area=radio*radio*3.14159265
        perimetro=(3.14159265*(radio*2))
        print("El area y perimetro de tu figura es de")
        print("AREA", area)
        print("PERIMETRO", perimetro)
    else:
        print("Syntax error, porfavor elige uno de los valores dados")
    continuar=input("Deseas realizar algun otro calculo rey (s/n): ")
