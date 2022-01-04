from tkinter import *
from module import *

root=Tk()

DisplayF=Label(root)
DisplayF.pack(fill=BOTH,expand=TRUE)

ListBoxLabel=Label(DisplayF, text="All Ent")
ListBox=Listbox(DisplayF, height = 10, width = 50, bg = "grey", activestyle = 'dotbox')



def ShowServiceOut():
    ServiceOut=Searching(Service="gmail", MasterID="TestID", con=conn)
    if ServiceOut != False:
        All=[]
        All.append(ServiceOut)
        N=0
        for i in All:
            ListBox.insert(N,f"{i}")
            N+=1
    else:
        pass
print(ShowServiceOut())

ListBoxLabel.pack()
ListBox.pack()



root.mainloop()