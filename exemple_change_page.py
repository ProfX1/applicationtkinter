# import tkinter module
from tkinter import Tk, Label, Button, Frame
 

# creating main tkinter window/toplevel
master = Tk()
master.title("griddemo4")
master.minsize(500, 250)
master.maxsize(500, 250)

def screen1():
    frame1 = Frame(master, width=500,height=250, bg='green')    
    frame1.place(x=0,y=0, width=500, height=250)

    lbl = Label(frame1,text='screen1')
    lbl.grid(row=0,column=0)

    btn2 = Button(frame1,text='Screen 2',command=screen2)
    btn2.grid(row=2,column=0)

    btn3 = Button(frame1,text='Screen 3',command=screen3)
    btn3.grid(row=3,column=0)

def screen2():
    frame2 = Frame(master, width=500,height=250,bg='red')    
    frame2.place(x=0,y=0, width=500, height=250)

    lbl = Label(frame2,text='screen2')
    lbl.grid(row=0,column=0)

    btn1 = Button(frame2,text='Screen 1',command=screen1)
    btn1.grid(row=1,column=0)

    btn3 = Button(frame2,text='Screen 3',command=screen3)
    btn3.grid(row=3,column=0)

def screen3():
    frame3 = Frame(master, width=500,height=250,bg='red')
    frame3.place(x=0,y=0, width=500, height=250)

    lbl = Label(frame3,text='screen3')
    lbl.grid(row=0,column=0)

    btn1 = Button(frame3,text='Screen 1',command=screen1)
    btn1.grid(row=1,column=0)

    btn2 = Button(frame3,text='Screen 2',command=screen2)
    btn2.grid(row=3,column=0)

screen1()
master.mainloop()