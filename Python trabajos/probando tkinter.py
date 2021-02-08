from tkinter import *



ventanita=Tk()
ventanita.title("Esta es la ventana principal")
ventanita.configure(bg="purple")
ventanita.geometry("500x500")
ventanita.resizable(False,False)


Label(ventanita, text="Ingrese su usuario",fg="black",font=("Arial", 30)).place(x=80,y=10)
dato="PEPe"
Entry(ventanita, textvariable=dato, font=("Arial",15), fg="white", bg="white").place(x=110, y=100)
Label(ventanita, text="Asi que tu nombre es: ",fg="White", bg="black",font=("Arial", 20)).place(x=110,y=200)
Label(ventanita, text=dato,fg="White", bg="black",font=("Arial", 20)).place(x=110,y=300)


#mostrando un mensaje





mainloop()