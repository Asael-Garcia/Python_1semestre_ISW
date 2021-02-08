#EXAMEN SEGUNDO PARCIAL
#GERARDO HERNÁDNEZ HERNÁNDEZ
import os

def validar(mensaje):
    bandera = True
    while bandera:
        try:
            valor = int(input(mensaje))
            bandera = False
        except:
            print ("\nSolamente se admiten números")
    return valor

def programa_principal():
    os.system("cls")
    print("CAJA REGISTRADORA")
    valorFinal = []
    banderaRegresar = True
    while banderaRegresar:
        arregloCliente = []
        articulos = validar("\n¿Cuántos artículos registrará para el cliente?: ")
        for articulos in range(articulos):
            precio = validar("\nIngrese el precio del producto vendido: $")
            arregloCliente.append(precio)
        continuar = str(input("\nPara ver el total del cliente y registrar a uno nuevo digite 0, \nPara terminar digite 00: \n"))

        if continuar == "0":
            valorsito = sum(arregloCliente)
            valorFinal.append(valorsito)
            print("El total del cliente es: $", valorsito)
            banderaRegresar = True
            enter = input("\nPresione ENTER para continuar y agregar al nuevo cliente\n")
            os.system("cls")

        elif continuar == "00":
            valorFinal.append(sum(arregloCliente))
            totalTodos = sum(valorFinal)
            print("\nEl total del día fue: $", totalTodos)
            contador = 1
            for i in (valorFinal):
                print("\nEl total del cliente ", contador," es: $", i)
                contador += 1
            banderaRegresar = False

        else:
            print("\nERROR")
            break

os.system("cls")
programa_principal()