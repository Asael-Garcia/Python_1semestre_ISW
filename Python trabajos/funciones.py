import os
def mi_funcion(cad,v=2,*algomas):#si le pongo el asterisco y luego la "variable" pyton
    #reconocera lo que este despues de ese * como una dupla
    print (cad*v)
    for cadena in algomas:
        print (cadena*v)

mi_funcion("Python ", 10, "Hola ", "Adios ", "n ", "cadenas ")
print ("\n")
print ("\n")
print ("\n")
print ("\n")
os.system ("cls")

def mi_funcion_dos (num1, num2):
    return (num1+num2)

resultado_de_suma = mi_funcion_dos(1,5)
print (resultado_de_suma)

