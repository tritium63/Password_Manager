from tkinter import *
from module import *
from tkWinSwitch import *

root=Tk()

Display=wiSet()

ListBoxLabel=Label(text="LogIn")
ListBox=Listbox(height = 10, width = 50, bg = "grey", activestyle = 'dotbox')
SearchBox=Entry(text="Enter Service Name")
Search=Button(text="Search", command= lambda : ShowServiceOut())
Exit=Button(text="Exit", command= lambda : Exit())


Display.addWi(ListBoxLabel)
Display.addWi(ListBox)
Display.addWi(SearchBox)
Display.addWi(Search)
Display.addWi(Exit)


Display.pack(ListBoxLabel)
Display.pack(ListBox)
Display.pack(SearchBox)
Display.pack(Search)
Display.pack(Exit)


def Exit():
    pass


def ShowServiceOut():
    ListBox.delete(0,END)
    Service=SearchBox.get()
    ServiceOut=Searching(Service, MasterID="TestID", con=conn)
    if ServiceOut != False:
        All=[]
        All.append(ServiceOut)
        N=0
        for i in All:
            ListBox.insert(N,f"{i}")
            N+=1
    if ServiceOut==False:
        ListBox.insert(0,"NO Result found !")
    else:
        pass


Display.create()

root.mainloop()