## Desarrollado por: Jose Alejandro Cardona V.

from InterpolacionNewton import *
from Tkinter import *

def Click():
    x = InterNewton(Text1.get())
    t2.set("Polinomio: ")
    t3.set(x.polinomio)
    x.graficar()

MainWindow = Tk()
MainWindow.geometry("400x400")
Label(MainWindow, text="Interpolacion de Newton", font=("Arial",16)).pack(expand=True, fill=X)
t1 = ""
Text1 = Entry(MainWindow, textvariable=t1)
Text1.insert(0, '(1,0),(0,1),(2,3),(-1,-2)')
Text1.pack(side=TOP, fill=X, expand=True)
Text1.focus()
BtnGraphic1 = Button(MainWindow, text='Graficar', command=Click).pack(fill=X, expand=True)
t2 = StringVar()
t3 = StringVar()
Text2 = Label(MainWindow, textvar=t2, font=("Arial",12)).pack(expand=True, fill=X)
Text3 = Label(MainWindow, textvar=t3, font=("Arial",14)).pack(expand=True, fill=X)

MainWindow.mainloop()