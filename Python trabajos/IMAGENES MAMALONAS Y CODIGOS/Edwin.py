#este es el de edwin


from tkinter import *

informe=Tk()
informe.title("El edwin")
informe.configure(bg="purple")
informe.geometry("500x500")
informe.resizable(True,True)


imagen1=PhotoImage(file="edwin4.png")
imagen2=PhotoImage(file="edwin2.png")
imagen3=PhotoImage(file="edwin3.png")
imagen3_a_la_mitad=imagen3.subsample(2,2)

Label(informe, image=imagen1).place(x=5,y=5)
Label(informe, image=imagen2).place(x=1100,y=5)
Label(informe, image=imagen3_a_la_mitad).place(x=5,y=500)

Label(informe, text="El Edwin", fg="white", bg="purple", font=("Goudy Stout",50)).place(x=400,y=100)

Label(informe, text="La cheve", fg="white",bg="purple",font=("Cooper Black", 40)).place(x=550,y=250)
Label(informe, text="como la ",fg="white",bg="purple", font=("Lucida Calligraphy", 40)).place(x=550,y=310)
Label(informe, text="verga,",fg="white",bg="purple", font=("Sitka Text", 40)).place(x=550,y=365)
Label(informe, text="hasta el ", fg="white",bg="purple", font=("Ink Free", 40)).place(x=550, y=440)
Label(informe, text="FONDO", fg="white", bg="purple", font=("Bernard MT Condensed", 40)).place(x=550,y=510)




mainloop()