from tkinter import *

from tkWinSwitch import *

root = Tk()

###login

set1 = wiSet()

l = Label(text="label of login page")

set1.addWi(l)

set1.pack(l,expand=TRUE)

btn = set1.addWi(Button(text="go to page 2 ",command=lambda :switch(set1,set2)))
######



###gen
set2 = wiSet()

l2 = set2.addWi(Label(text="label of genrator"))

set2.grid(l2,row=0,column=0)

btn2 = set2.addWi(Button(text="go to page 1 ",command=lambda :switch(set2,set1)))

set2.grid(btn2,row=1,column=0)
########

set1.create()


root.mainloop()