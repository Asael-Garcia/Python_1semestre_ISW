#este es para la galtzia

from tkinter import *

galatzia=Tk()
galatzia.title("Este es para ti galatzia")
galatzia.geometry("500x500")
galatzia.configure(bg="VioletRed1")
galatzia.resizable(True,True)

imagen1=PhotoImage(file=)
imagen2=PhotoImage(file=)

#titulo
Label(galatzia, text="La Galatzia", fg="white",bg="VioletRed1", font=("Showcard Gothic", 70)).place(x=550,y=100)

#mensaje
Label(galatzia, text="Si por pendeja",fg="White", bg="VioletRed1", font=("Bernard MT Condensed", 40)).place(x=550, y=250)
Label(galatzia, text="me cai, ", bg="VioletRed1", fg="white", font=("Lucida Calligraphy", 40)).place(x=550,y=310)
Label(galatzia, text="Por cabrona ",bg="VioletRed1", fg="white", font=("Goudy Stout", 40)).place(x=550, y=370)
Label(galatzia, text="me levanto", bg="VioletRed1", fg="White", font=("Old English Text MT", 40)).place(x=550,y=430)



mainloop()