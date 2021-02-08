#este es para el kevin


from tkinter import *

ventana=Tk()
ventana.title("El Kevin")
ventana.geometry("500x500")
ventana.configure(bg="YellowGreen")
ventana.resizable(True,True)

imagen1=PhotoImage(file=)
imagen2=PhotoImage(file=)


#titulo
Label(ventana, text="El Kevin", fg="Black", bg="YellowGreen", font=("Old English Text MT", 70)).place(x=550,y=100)

#mensaje
Label(ventana, text="Izquierda o ", fg="Black", bg="YellowGreen", font=("Bernard MT Condensed", 40)).place(x=550,y=250)
Label(ventana, text="derecha", fg="black", bg="YellowGreen", font=("Lucida Calligraphy", 40)).place(x=550, y=310)
Label(ventana, text="todo es ",bg="YellowGreen", fg="Black", font=("Matura MT Script Capitals", 40)).place(x=550, y=370)
Label(ventana, text="igual", fg="black", bg="YellowGreen", font=("Informal Roman", 40)).place(x=550, y=430)

mainloop()