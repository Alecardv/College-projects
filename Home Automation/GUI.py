"""
@author: J. Alejandro Cardona
"""

from Tkinter import *
import Tkinter
from Control import *
from PIL import Image, ImageTk

control = Control()

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.house = Toplevel()
        self.textvar = StringVar()
        self.initUI()
        self.initHouse()

    def initUI(self):
        self.parent.title("Home Interaction")
        self.pack(fill=BOTH, expand=1)
        
        frame1 = Frame(self)
        frame1.pack(fill=BOTH, expand=True)
        lbl1 = Label(frame1, text="Bienvenido", font=("Arial", 16))
        lbl1.pack(padx=5, pady=5, fill=X)
        lbl1 = Label(frame1, justify=LEFT, anchor=W, text="Esta es la interface de interaccion con Alice\n su asistente de hogar.", font=("Arial", 12))
        lbl1.pack(padx=5, pady=5, fill=X)
        self.txt = Text(frame1)
        self.txt.pack(fill=BOTH, pady=10, padx=10, expand=True) 

        frame2 = Frame(self)
        frame2.pack(fill=X)
        entry1 = Entry(frame2, textvariable=self.textvar)
        entry1.pack(fill=X, side=LEFT, pady=10, padx=10, expand=True)
        SendButton = Button(frame2, text="Enviar", command=self.send_btn)
        SendButton.pack(side=RIGHT, pady=5, padx=5)

    def initHouse(self):
        self.house.title('House Graph')
        self.house.geometry('510x710')

        border = PhotoImage(file="border.gif")
        door_garage = PhotoImage(file='door.gif')
        door_roomn = PhotoImage(file='door.gif')
        door_roomp = PhotoImage(file='door.gif')
        door_hall = PhotoImage(file='door.gif')
        door_kitchen = PhotoImage(file='door.gif')
        door_livingroom = PhotoImage(file='door.gif')
        lightoff_garage = PhotoImage(file='light-off.gif')
        lightoff_roomn = PhotoImage(file='light-off.gif')
        lightoff_roomp = PhotoImage(file='light-off.gif')
        lightoff_hall = PhotoImage(file='light-off.gif')
        lightoff_kitchen = PhotoImage(file='light-off.gif')
        lightoff_livingroom = PhotoImage(file='light-off.gif')
        lighton_garage = PhotoImage(file='light-on.gif')
        lighton_roomn = PhotoImage(file='light-on.gif')
        lighton_roomp = PhotoImage(file='light-on.gif')
        lighton_hall = PhotoImage(file='light-on.gif')
        lighton_kitchen = PhotoImage(file='light-on.gif')
        lighton_livingroom = PhotoImage(file='light-on.gif')

        self.lbl_border = Label(self.house, image=border)
        self.lbl_door_garage = Label(self.house, image=door_garage)
        self.lbl_door_roomn = Label(self.house, image=door_roomn)
        self.lbl_door_roomp = Label(self.house, image=door_roomp)
        self.lbl_door_hall = Label(self.house, image=door_hall)
        self.lbl_door_kitchen = Label(self.house, image=door_kitchen)
        self.lbl_door_livingroom = Label(self.house, image=door_livingroom)
        self.lbl_lightoff_garage = Label(self.house, image=lightoff_garage)
        self.lbl_lightoff_roomn = Label(self.house, image=lightoff_roomn)
        self.lbl_lightoff_roomp = Label(self.house, image=lightoff_roomp)
        self.lbl_lightoff_hall = Label(self.house, image=lightoff_hall)
        self.lbl_lightoff_kitchen = Label(self.house, image=lightoff_kitchen)
        self.lbl_lightoff_livingroom = Label(self.house, image=lightoff_livingroom)
        self.lbl_lighton_garage = Label(self.house, image=lighton_garage)
        self.lbl_lighton_roomn = Label(self.house, image=lighton_roomn)
        self.lbl_lighton_roomp = Label(self.house, image=lighton_roomp)
        self.lbl_lighton_hall = Label(self.house, image=lighton_hall)
        self.lbl_lighton_kitchen = Label(self.house, image=lighton_kitchen)
        self.lbl_lighton_livingroom = Label(self.house, image=lighton_livingroom)

        self.lbl_border.image = border
        self.lbl_door_garage.image = door_garage
        self.lbl_door_roomn.image = door_roomn
        self.lbl_door_roomp.image = door_roomp
        self.lbl_door_hall.image = door_hall
        self.lbl_door_kitchen.image = door_kitchen
        self.lbl_door_livingroom.image = door_livingroom
        self.lbl_lightoff_garage.image = lightoff_garage
        self.lbl_lightoff_roomn.image = lightoff_roomn
        self.lbl_lightoff_roomp.image = lightoff_roomp
        self.lbl_lightoff_hall.image = lightoff_hall
        self.lbl_lightoff_kitchen.image = lightoff_kitchen
        self.lbl_lightoff_livingroom.image = lightoff_livingroom
        self.lbl_lighton_garage.image = lighton_garage
        self.lbl_lighton_roomn.image = lighton_roomn
        self.lbl_lighton_roomp.image = lighton_roomp
        self.lbl_lighton_hall.image = lighton_hall
        self.lbl_lighton_kitchen.image = lighton_kitchen
        self.lbl_lighton_livingroom.image = lighton_livingroom

        self.lbl_border.pack(padx=5, pady=5)
        self.lbl_door_garage.pack(padx=5, pady=5)
        self.lbl_door_roomn.pack(padx=5, pady=5)
        self.lbl_door_roomp.pack(padx=5, pady=5)
        self.lbl_door_hall.pack(padx=5, pady=5)
        self.lbl_door_kitchen.pack(padx=5, pady=5)
        self.lbl_door_livingroom.pack(padx=5, pady=5)
        self.lbl_lightoff_garage.pack(padx=5, pady=5)
        self.lbl_lightoff_roomn.pack(padx=5, pady=5)
        self.lbl_lightoff_roomp.pack(padx=5, pady=5)
        self.lbl_lightoff_hall.pack(padx=5, pady=5)
        self.lbl_lightoff_kitchen.pack(padx=5, pady=5)
        self.lbl_lightoff_livingroom.pack(padx=5, pady=5)
        self.lbl_lighton_garage.pack(padx=5, pady=5)
        self.lbl_lighton_roomn.pack(padx=5, pady=5)
        self.lbl_lighton_roomp.pack(padx=5, pady=5)
        self.lbl_lighton_hall.pack(padx=5, pady=5)
        self.lbl_lighton_kitchen.pack(padx=5, pady=5)
        self.lbl_lighton_livingroom.pack(padx=5, pady=5)

    def send_btn(self):
        msg = self.textvar.get()
        self.txt.tag_configure('you', font=('Arial', 11, 'bold'))
        self.txt.tag_configure('she', font=('Arial', 11, 'bold'), foreground='#ff0000')
        self.txt.tag_configure('text', font=('Arial', 11, 'normal'))
        self.txt.insert(INSERT, "Tu: ", 'you')
        self.txt.insert(END, msg+'\n', 'text')
        reply = control.interact(msg)
        self.txt.insert(INSERT, "Alice: ", 'she')
        self.txt.insert(END, reply+'\n', 'text')
        self.textvar.set("")

def MainWindow():
    root = Tk()
    root.geometry('400x600')
    app = GUI(root)
    root.mainloop()

if __name__ == '__main__':
    MainWindow()