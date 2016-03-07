## Desarrollado por: Jose Alejandro Cardona V.
## Metodos Numericos: Aproximacion por minimos cuadrados

from Tkinter import *
from AproxMinCuad import *

def BtnClick(): #Boton de Aproximacion lineal
    x = AproxLineal(TextBox.get()) #Obtiene las coordenadas que se escribieron en la caja de texto
    txt1.set("Lineal:") # Establece el texto de la aproximacion
    txt2.set(str(x.Result.item(0))+" + "+str(x.Result.item(1))+"x") # Establece el texto de la ecuacion
    x.plot()#Muestra el grafico

def BtnClick2(): #Boton de Aproximacion cuadratica
    x = AproxCuadratica(TextBox.get())#Obtiene las coordenadas que se escribieron en la caja de texto
    txt1.set("Cuadratica:")# Establece el texto de la aproximacion
    txt2.set(str(x.Result.item(0)) + " + " + str(x.Result.item(1)) + "x + " + str(x.Result.item(2)) + "x^2")# Establece el texto de la ecuacion
    x.plot() #Muestra el grafico

def BtnClick3(): #Boton de Aproximacion exponencial
    x = AproxExponencial(TextBox.get())#Obtiene las coordenadas que se escribieron en la caja de texto
    txt1.set("Exponencial:")# Establece el texto de la aproximacion
    txt2.set(str(x.LA)+" * "+str(x.LB)+"^x")# Establece el texto de la ecuacion
    x.plot()#Muestra el grafico

MainWindow = Tk() #Crea la ventana principal
MainWindow.geometry("400x500") #Establece el tamano de la ventana

Label(MainWindow, text="Ingrese las Coordenadas, Ej: (1,2), (3,4), ... (x,y)").pack(expand=True, fill=X)

xy = "" #Donde se guardan las coordenadas que el usuario escribe en la caja de texto
TextBox = Entry(MainWindow, textvariable=xy) #la caja de texto
TextBox.insert(0, '(1,3), (-2,4), (7,0)') #Valores iniciales para la caja de texto
TextBox.pack(side=TOP, fill=X, expand=True) #Mostrar la caja de texto
TextBox.focus() #Que el teclado haga foco sobre la caja de texto

BtnGraphic1 = Button(MainWindow, text='Aproximacion lineal', command=BtnClick) #boton
BtnGraphic2 = Button(MainWindow, text='Aproximacion cuadratica', command=BtnClick2) #boton
BtnGraphic3 = Button(MainWindow, text='Aproximacion exponencial', command=BtnClick3) #boton
BtnGraphic1.pack(fill=X, expand=True) #Mostrar boton
BtnGraphic2.pack(fill=X, expand=True) #Mostrar boton
BtnGraphic3.pack(fill=X, expand=True) #Mostrar boton

txt1 = StringVar() #Donde se guarda el texto del Label 
txt2 = StringVar() #Donde se guarda el texto del Label 
TextResult = Label(MainWindow, textvar=txt1).pack(expand=True, fill=X) #El label (El nombre de la aproximacion)
TextResult = Label(MainWindow, textvar=txt2).pack(expand=True, fill=X) #El label (La ecuacion)

MainWindow.mainloop() #Iniciar todo el entorno grafico.