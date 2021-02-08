#ORDENAMIENTO POR MEZCLA
import os
import random

#SE DEFINE LA FUNCIÓN DEL METODO
def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        primera_mitad = lista[:mitad]
        segunda_mitad = lista[mitad:]

        merge_sort(primera_mitad)
        merge_sort(segunda_mitad)
        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad):
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else:
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1
        
        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1

        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1

os.system ("cls")
#numeros = [random.randint(1, 100000) for _ in range (10)]
#print("LISTA ORIGINAL: ", numeros)
numeros = []
print("Ingresa la cantidad de números que tendrá tu lista: ")
j = int(input())

for contador in range (0,j):
    print ("Ingresa el dato numero ", contador , " : ")
    numerito=int(input())
    numeros.append(numerito)

print("LISTA ORIGINAL: ", numeros)

merge_sort(numeros)
print("\nLISTA ORDENADA: ", numeros)
