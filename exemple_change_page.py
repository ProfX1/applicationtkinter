from tkinter import IntVar, StringVar, Tk, Label, Button, Frame, OptionMenu, Radiobutton, Menu, Menubutton, Checkbutton,filedialog
from tkinter import Label,Entry,Text

from tkinter import ttk
 
def coucou():
    print("coucou")

master = Tk()
master.title("griddemo0: placer avec grid")

l1 = Label(master, text = "bouton de base:")
l1.grid(row = 0, column = 0, pady = 2)

b1 = Button(master, text = "bouton simple", command=coucou)
b1.grid(row = 0, column = 1, pady = 2)

l2 = ttk.Label(master, text = "bouton avance:")
l2.grid(row = 0, column = 2, pady = 2)
 
b2 = ttk.Button(master, text = "button2", command=coucou)
b2.grid(row = 0, column = 3, pady = 2)


l1 = Label(master, text = "zone de texte de base:")
l1.grid(row = 1, column = 0, pady = 2)

b1 = Entry(master)
b1.grid(row = 1, column = 1, pady = 2)

l2 = ttk.Label(master, text = "zone de texte avance:")
l2.grid(row = 1, column = 3, pady = 2)
 
b2 = ttk.Entry(master)
b2.grid(row = 1, column = 4, pady = 2)


l3 = Label(master, text = "zone de texte large:")
l3.grid(row = 4, column = 0, pady = 2)

b3 = Text(master, width=20, height=3)
b3.grid(row = 4, column = 1, pady = 2)


l4 = Label(master, text = "menu deroulant de base:")
l4.grid(row = 5, column = 0, pady = 2)

options = ["option1", "option2", "option3"]
clicked = StringVar()
drop = OptionMenu( master , clicked , *options )
drop.grid(row = 5, column = 1, pady = 2)

l5 = Label(master, text = "menu deroulant avance:")
l5.grid(row = 5, column = 2, pady = 2)

drop2 = ttk.OptionMenu( master , clicked , *options )
drop2.grid(row = 5, column = 3, pady = 2)

l6 = Label(master, text = "radio de base:")
l6.grid(row = 6, column = 0, pady = 2)

var = IntVar()
radio = Radiobutton(master, text='radio1', value=1, variable=var)
radio.grid(row = 6, column = 1, pady = 2)

radio2 = Radiobutton(master, text='radio2', value=2, variable=var)
radio2.grid(row = 7, column = 1, pady = 2)


l7 = Label(master, text = "radio de avance:")
l7.grid(row = 6, column = 0, pady = 2)

radio3 = ttk.Radiobutton(master, text='radio1', value=1, variable=var)
radio3.grid(row = 6, column = 3, pady = 2)

radio4 = ttk.Radiobutton(master, text='radio2', value=2, variable=var)
radio4.grid(row = 7, column = 3, pady = 2)


l8 = Label(master, text = "checkbox:")
l1.grid(row = 8, column = 0, pady = 2)

cvalue  =IntVar()
c1 = Checkbutton(master, text = "check me", command=coucou, variable=cvalue)
c1.grid(row = 8, column = 1, pady = 2)

c2 = ttk.Checkbutton(master, text = "check me avance", variable=cvalue)
c2.grid(row = 8, column = 3, pady = 2)


master.mainloop()