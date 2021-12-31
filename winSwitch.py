from tkinter import *


def switch(a,b):
    exec(f"root{a}.destroy()")
    exec(f"fw{b}()")

def fw1():
    global root1
    root1 = Tk()
    root1.geometry("500x500")
    btn = Button(root1,text="first",command=lambda :switch(1,2))
    btn.pack()
    root1.mainloop()

def fw2():
    global root2
    root2 = Tk()
    root2.geometry("500x500")
    btn = Button(root2,text="second",command=lambda :switch(2,1))
    btn.pack()
    root2.mainloop()

fw1()