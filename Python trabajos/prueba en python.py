continuar = "s"
while (continuar == "s"):
    base = float(input("Indica la medida de la base: "))
    altura = float(input("Indica la medida de la altura: "))
    area = base * altura
    print ("El area del rectangulo es: ", area , " cm2")
    continuar = input ("Desea realizar otro calculo: ")
