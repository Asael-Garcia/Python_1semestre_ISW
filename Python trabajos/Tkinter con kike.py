#tkinter con kike

from tkinter import *

ventana=Tk()#crea una ventana, pero la cierra rapidamente sin el mainloop
ventana.title("---Que paso parcero---")#titulo de la ventana
ventana.geometry("600x300")#ancho y alto de la ventana
ventana.resizable(True,True)#para no poder redimencionar la ventana, se quede solamente como la pongo yo
ventana.configure(background="thistle4")


Label(ventana, text="Hola mundo",font=("Arial",20),fg="white", bg="#f77559").place(x=200, y=150)
#hago un mensaje con label(), primero indico en qe ventana, luego el texto, lo igualo a lo que va a ser, despues un .place para donde va ir con .place(x and y)
#otros detalles esteticos es despues del texto, donde esta el font(), donde primero digo que tipo de fuente quiero, y despues el tamañno de la letra, son cosas esteticas
#otra cosa estetita es fg que es el color de fuente, ademas del bg, para alterar el fondo de, en este caso el texto que estamos escribiendo, pero tambien aplica ara cuadros 

dato=""
Entry(ventana, textvariable=dato, font=("Arial",15), fg="white", bg="black").place(x=220, y=200)
#el Entry sirve para la entrada de informacion, de manera que primero pongo Entry("la ventana donde entrara la informacion") y despues con un .place(x and y) situo donde entrará la info

Button(ventana, text="Push me mami", bg="Black",fg="White").place(x=350,y=550)
#para crear un boton con el que se pueda interactuar, de igaul manera esta vez solo se pone Button("todos los datos, igual a label").place(cooredenadas)

img=PhotoImage(file="bob.png")#guardo en una variable la imagen que usare, en este caso es una imagen de bob esponja cholo
Label(ventana, image=img).place(x=250,y=250)#imprimi la imaagen con un Label(ventana e image=nombre de la variable donde guarde la imagen).place(coordenadas)
Label(ventana, text="10 de 10 kike", font=("Arial", 30), fg="white", bg="Black").place(x=250,y=450)

mainloop()#para que todo lo que este encima de el este en un bucle