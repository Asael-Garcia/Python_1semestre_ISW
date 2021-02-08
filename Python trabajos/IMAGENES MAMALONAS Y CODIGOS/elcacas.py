

from tkinter import *

ventanita=Tk()
ventanita.title("El Cacas")
ventanita.configure(background="pink")
ventanita.geometry("1000x1000")
ventanita.resizable(True,True)

#imagenes
imagen=PhotoImage(file="2.png")
imagen2=PhotoImage(file="1.png")
#titulo
Label(ventanita, text="El Gonza", fg="black",bg="Pink",font=("Copperplate Gothic Bold", 70)).place(x=500,y=100)

#poner imagen
Label(ventanita, image=imagen, height=700, width= 400).place(x=5,y=5)
Label(ventanita, image=imagen2, height=700, width= 400).place(x=1000,y=5)

Label(ventanita, text="Si no hay pisto",fg="black",bg="pink",font=("Lucida Calligraphy", 30)).place(x=500,y=250)
Label(ventanita, text="no asisto", fg="Black", bg="pink", font=("Goudy Stout",30)).place(x=500,y=300)
Label(ventanita, text="primero tomo", fg="Black",bg="pink", font=("Chiller", 30)).place(x=500,y=350)
Label(ventanita, text="luego existo",fg="Black", bg="pink", font=("Algerian", 30)).place(x=500,y=400)



mainloop()