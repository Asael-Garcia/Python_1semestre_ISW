from tkinter import *

ventanita=Tk()
ventanita.title("Esta es otra prueba para ver como va la onda de esto")
ventanita.geometry("600x600")
ventanita.resizable(True,True)
ventanita.configure(background="black")

imagenAnchuraMaxima=400
imagenAlturaMaxima=700

ojos=PhotoImage(file="ojos.png")
manos=PhotoImage(file="manos.png")
imagen=PhotoImage(file="FANI PELONA.png")

Label(ventanita, text="FANI PELONA", font=("Goudy Stout", 40), fg="white", bg="black").place(x=450,y=100)
Label(ventanita, image=imagen, width=imagenAnchuraMaxima, height=imagenAlturaMaxima).place(x=10,y=10)

Label(ventanita, text="El arte se ve", font=("Kristen ITC", 35), fg="white", bg="black").place(x=450,y=250)
Label(ventanita, text="con los ojos,", fg="white",bg="black",font=("Lucida Calligraphy", 35)).place(x=450,y=350)
Label(ventanita, image=ojos, width=200, height= 100 ).place(x=750,y=300)
Label(ventanita, text="y los pelones", fg="white", bg="black",font=("Tempus Sans ITC", 35)).place(x=450,y=450)
Label(ventanita, text="con la mano.",fg="white",bg="black",font=("Snap ITC", 35)).place(x=450,y=550)
Label(ventanita, image=manos, width= 400, height= 300).place(x=850, y=450)
mainloop()