continuar="s"
print ("Bienvenido a la comprabadora de numeros primos")
print ("Digitaliza un numero y te diremos si es primo o no")
while continuar=="s":
    print ("Ahora, porfavor, dame el numero")
    numerito=int(input())
    contador=0
    for i in range (2, numerito):
        
        if (numerito%i==0):
           contador +=1

    if contador>=1:
        print (numerito," no es un numero primo")
    else:
        print (numerito, " es un numero primo")
    print ("Deseas seguir calculando? (s/n)")
    continuar=input()
    
        
