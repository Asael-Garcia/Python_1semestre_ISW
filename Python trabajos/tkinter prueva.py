#nuevo tkinter para mi

from tkinter import * 


ventana=Tk()
ventana.title("Hola primer demo")
ventana.geometry("600x300")
ventana.resizable(True,True)
ventana.configure(background="purple")

burbuja=Tk()
burbuja.title("Bubuja")
burbuja.geometry("600x300")
burbuja.resizable(False,False)
burbuja.configure(background="blue")


bellota=Tk()
bellota.title("Bellota que más guacho")
bellota.geometry("600x300")
bellota.resizable(False,False)
bellota.configure(background="green")



laroja=Tk()
laroja.title("La roja por que bonbon no funciona")
laroja.geometry("600x200")
laroja.resizable(False,False)
laroja.configure(background="red")


Label(ventana, text="Hola mundo agin, simon como la ves", font= ("Arial",50), fg="black").place(x=150,y=250)
Label(burbuja, text="Holo muundo pero esta ves mas o menos algo asi como la ves", font=("Arial", 20), fg="black").place(x=150, y=200)
mainloop()