import os
print("Hola mundo")

def mostrar(resultado):
    for i in range (0,len(resultado)):
            print (resultado[i])


def solapa():
    resultado=[]
    continuar="s"
    while continuar=='s':
        numerito=int(input("Dame cualquier numero y te hare las tablas de multiplicar de este mismo, ademas de guardarlas en un array: "))
        for i in range(0,numerito+1):
            salida= i * numerito
            resultado.append(salida)
            print(i, "*", numerito, "=", salida)
        continuar=input("¿Deseas volver a realizar la tabla de algun otro numero? s/n: ")
        os.system("cls")
    print("Perfecto entonces te mostrare el array (arrreglo)")
    print("Este es el array en forma de lista: ")
    mostrar(resultado)
    continuar=(input("Presiona enter para continuar"))

solapa()
    