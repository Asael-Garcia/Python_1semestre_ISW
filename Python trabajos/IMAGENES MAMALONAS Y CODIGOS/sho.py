#este es para mi guacho

from tkinter import *

ventana=Tk()
ventana.title("Este es para mi si o si")
ventana.configure(bg="gray")
ventana.geometry("500x500")
ventana.resizable(True,True)

imagen1=PhotoImage(file=)
imagen2=PhotoImage(file=)

#titulo
Label(ventana, text="El Moni", fg="Black", bg="gray", font=("Engravers MT", 70)).place(x=470, y=100)

#mensaje
Label(ventana, text="Prefiero probar", bg="gray",fg="black", font=("Showcard Gothic",40)).place(x=500,y=250)
Label(ventana, text="el sabor de la", bg="gray", fg="black", font=("Matura MT Script Capitals", 40)).place(x=500,y=310)
Label(ventana, text="verga, antes que", fg="black", bg="gray", font=("Informal Roman", 40)).place(x=500, y=370)
Label(ventana, text="tomar alcohol caro,", bg="gray",fg="black",font=("Bernard MT Condensed", 40)).place(x=500,y=430)
Label(ventana, text="no sea culo", fg="black", bg="gray", font=("Old English Text MT", 40)).place(x=500,y=490)
Label(ventana, text="compa", fg="black", bg="gray", font=("Goudy Stout", 40)).place(x=500,y=550)
Label(ventana, text="me vas a dejar abajo jade?", fg="black", bg="gray", font=("Lucida Calligraphy", 30)).place(x=450,y=650)


mainloop()