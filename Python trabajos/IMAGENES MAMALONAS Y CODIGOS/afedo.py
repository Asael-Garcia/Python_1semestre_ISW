
from tkinter import *

ventanita=Tk()
ventanita.title("El Afedineitor")
ventanita.configure(bg="blue")
ventanita.geometry("500x500")



#titulo
Label(ventanita, text="El Afedo", fg="white", bg="blue", font=("Old English Text MT", 80)).place(x=550,y=30)


imagen1=PhotoImage(file="afedo2.png")
imagen2=PhotoImage(file="afedo3.png")
imagen3=PhotoImage(file="afedo1.png")

imagen_a_la_mitad=imagen1.subsample(2,2)
imagen3_a_la_mitad=imagen3.subsample(2,2)

Label(ventanita, image=imagen_a_la_mitad).place(x=5,y=5)
Label(ventanita, image=imagen2).place(x=1000,y=5)
Label(ventanita, image=imagen3_a_la_mitad).place(x=900,y=420)

#texto
Label(ventanita, text="Un dia estas", fg="white",bg="blue",font=("Copperplate Gothic Bold", 30)).place(x=500,y=250)
Label(ventanita, text="pedo, y al", fg="white",bg="blue",font=("Snap ITC", 30)).place(x=500,y=300)
Label(ventanita, text="otro tambien,", fg="white", bg="blue", font=("Goudy Stout", 30)).place(x=500,y=350)
Label(ventanita, text="arriba", fg="white",bg="blue",font=("Forte", 30)).place(x=500,y=400)
Label(ventanita, text="EL CRUZ AZUL", fg="white", bg="blue", font=("Lucida Calligraphy", 30)).place(x=500,y=450)



mainloop()