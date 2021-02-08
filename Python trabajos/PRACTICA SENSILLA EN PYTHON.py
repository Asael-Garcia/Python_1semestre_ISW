#PRACTICA SENSILLA EN PYTHON 

#funcion para hacer los calculos
def suma(numero1,numero2):
    return numero1 + numero2, numero1* numero2

def principal():
    a=float(input("Dame el primer numero: "))
    b=float(input("Dame el segundo numero: "))
    s=suma(a,b)#la funcion suma la guardo en la variable s, al igual que en ruby python me almaceno los dos "retuns" en un vectos
    #para poder imprimirlos despues solo imrpimo la variable donde esta este vector que me genero y la posicion del resultado que quiero ver

    print ("La suma de ambos numeros es de: ",s[0], " y la multiplicacion es de: ",s[1])
    #aqui los imrpimo en la pocicion del vector que deseo

principal()