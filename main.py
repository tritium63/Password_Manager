#importing modules
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from module import *
from tkWinSwitch import *


root=Tk()
#functions for buttons and other widgets
def SubmitFn():
    global MasterID
    MID=userentry.get()
    MPWD=passentry.get()
    print(MID, MPWD)
    if UserVerification(MID,MPWD,conn):
        switch(set1,set2)
        MasterID = MID
        uservalue.set('')
        passvalue.set('')
    else:
        print("Opps")        



#title
root.geometry("1200x700")
root.title("Password Manager - Login Page")

set1 = wiSet()
#setting background image
bgImage=Image.open("Background Design - Password Manager.jpg") 
bgImageTk= ImageTk.PhotoImage(bgImage)
bgLabel = Label(image=bgImageTk)
set1.addWi(bgLabel)
set1.pack(bgLabel,fill=BOTH,expand=TRUE)

#login widget
loginLabel=set1.addWi(Label(bgLabel,bg="black"))
set1.place(loginLabel,rely=0.5,relx=0.5,anchor=CENTER)

#variables for fonts used
usualfont_tuple=("Comic Sans MS",12,"bold")
headFont_tuple=("Comic Sans MS",16,"bold")

#Welcome Text 
welText=set1.addWi(Label(loginLabel, text="Welcome To Password Manager", font =headFont_tuple, bg="black",fg="white"))
set1.grid(welText,row=0,column=1)

#taking entries of username and password
username=set1.addWi(Label(loginLabel, text="Username: ",font=usualfont_tuple,bg="black",fg="white",pady=12,padx=12))
password=set1.addWi(Label(loginLabel,text="Paswword: ",font=usualfont_tuple,bg="black",fg="white"))
set1.grid(username,row=1,column=0)
set1.grid(password,row=2,column=0)

uservalue=StringVar()
passvalue=StringVar()

userentry=set1.addWi(Entry(loginLabel, textvariable=uservalue,width=40 ))
passentry=set1.addWi(Entry(loginLabel,textvariable=passvalue,width=40))
set1.grid(userentry,row=1,column=1,padx=10)
set1.grid(passentry,row=2,column=1,padx=10)




#Creating submit button
submitBtn=set1.addWi(Button(loginLabel, bg="grey", text="LOGIN",fg="white",command=SubmitFn))
set1.grid(submitBtn,row=3,column=1)

set1.create()


# createing the menu page

def logout():
    global MasterID
    switch(set2,set1)
    MasterID = ""
set2 = wiSet()

btn1 = set2.addWi(Button(root,text="log out",command=logout))
btn2 = set2.addWi(Button(root,text="retrieve password",command = lambda :switch(set2,Display)))
btn3 = set2.addWi(Button(root,text="add record"))

set2.pack(btn1)
set2.pack(btn2)
set2.pack(btn3)


Display=wiSet()

ListBoxLabel=Label(text="LogIn")
ListBox=Listbox(height = 10, width = 50, bg = "grey", activestyle = 'dotbox')

sBox = StringVar()
SearchBox=Entry(text="Enter Service Name",textvariable=sBox)


Search=Button(text="Search", command= lambda : ShowServiceOut())
Exit=Button(text="Go Back", command= lambda : Exit())


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
    ListBox.delete(0,END)
    sBox.set('')
    switch(Display,set2)
    


def ShowServiceOut():
    ListBox.delete(0,END)
    Service=SearchBox.get()
    ServiceOut=Searching(Service, MasterID, con=conn)
    if ServiceOut != False:
        All=[]
        All.append(ServiceOut)
        N=0
        for i in All:
            ListBox.insert(N,f"{i}")
            N+=1
    else:
        pass
    if not ServiceOut:
        ListBox.insert(0,"no result found")
root.mainloop()
