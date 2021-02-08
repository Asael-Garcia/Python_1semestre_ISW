continuar="s"#le asigno a la variable continuar el valor de "s"
print ("Bienvenido a la calculadora de tablas de multiplicar") #doy un mensaje de binvenida
while (continuar=="s"): #inicio el proceso While o mientras, el cual se repetira todo lo interior mientas continuar sea igula a s
        print ("Nota: Esta calculadora solo mostrara los resultados de tu numero dentro de un multiplo en un rango del 1-10")#añado una nota sobre lo que hara la calculadora
        numero=float(input("¿De que numero quieres ver la tabla?: "))#dentro de la misma linea muestro un mensae preguntado cual es el numero del que quieres conocer las tablas
        #y ademas le asigno el valor de flotante al numero que se digitara
        for contador in range(1,11):#inicio el proceso para, donde contenedor, en un rango de 1-11 hara una cuenta de uno en uno
            numero_final= numero * contador#a nuemer_final le añado el valor del numero digitado antes por el contador
            print (numero,("*"), range, ("="),numero_final)#imprimo el mensaje donde aparecera primero el numero, luego * dentro de comillas despues el rango que corresponda
            #despues del rango aparecera un igual y al final el resultado de la multiplicacion segun el rango

        continuar= (input ("¿Quieres seguir calculando?: "))#regreso la tabulacion un poco y dentro de la misma linea pregunto si desea continuar, la respuesta sera nuestro
        #continuar y segun esta se repetiria el proceso dentro de while o no
    
        
