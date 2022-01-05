#importing modules
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from module import *
from tkWinSwitch import *
from tkinter import messagebox
from PasswordGen import *

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
btn3 = set2.addWi(Button(root,text="add record", command=lambda :switch(set2, genSet)))

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

def ShowPass():
    Pass.set(PassGen())
MasterID="TempID"

def passvals():
    TempPass=PasswordEntry.get()
    TempService=serviceNameval.get()
    UIDD=userIDval.get()
    if TempService=="" or UIDD=="" or TempPass=="":
        messagebox.showerror("Invalid Input", "Feilds Cannot be Empty")
    else:
        addData(MasterID,TempService, UIDD, TempPass, conn)

#creating set for generator page 
genSet=wiSet()

#fonts
headfont_tuple=("Comic Sans MS",16,"bold")
generalFont=("Comic Sans MS",12,"bold")

#setting background
bgImage=Image.open("Background Design - Password Manager.jpg") 
bgImageTk= ImageTk.PhotoImage(bgImage)
bgLabel = Label(image=bgImageTk)
genSet.addWi(bgLabel)
genSet.pack(bgLabel,fill=BOTH,expand=TRUE)



generatorWidget=Label(bgLabel,bg="black")
# generatorWidget.place(relx=0.5,rely=0.5,anchor=CENTER)
genSet.addWi(generatorWidget)
genSet.place(generatorWidget, relx=0.5,rely=0.5, anchor=CENTER)
# Heading Text
headText=Label(generatorWidget,text="New UID and Password Generation", font=headfont_tuple,bg="black",fg="white",padx=30)
# headText.grid(row=0,column=1)
genSet.addWi(headText)
genSet.grid(headText,row=0,column=1)

# #entry fields
userID=Label(generatorWidget,text="User ID:",font=generalFont,bg="black",fg="white",pady=10)
# userID.grid(row=1,column=0)
genSet.addWi(userID)
genSet.grid(userID,row=1,column=0)


passWord=Label(generatorWidget,text="Password:",font=generalFont,bg="black",fg="white")
# passWord.grid(row=2,column=0)
genSet.addWi(passWord)
genSet.grid(passWord,row=2,column=0)

Pass=StringVar()

PasswordEntry=Entry(generatorWidget, width=75, textvariable=Pass)
genSet.addWi(PasswordEntry)
genSet.grid(PasswordEntry,row=2,column=1,columnspan=2)


serviceName=Label(generatorWidget,text="Service Name:",font=generalFont,bg="black",fg="white",pady=10)
# serviceName.grid(row=3,column=0)
genSet.addWi(serviceName)
genSet.grid(serviceName,row=3,column=0)


userIDval=Entry(generatorWidget,width=75)
# userIDval.grid(row=1,column=1)
genSet.addWi(userIDval)
genSet.grid(userIDval,row=1,column=1,columnspan=2)

serviceNameval=Entry(generatorWidget,width=75)
# serviceNameval.grid(row=3,column=1)
genSet.addWi(serviceNameval)
genSet.grid(serviceNameval,row=3,column=1,columnspan=2)
#submit button
submitBtn=Button(generatorWidget,text="Submit",bg="grey",fg="white",command=passvals)
# submitBtn.grid(row=4,column=1,pady=10)
genSet.addWi(submitBtn)
genSet.grid(submitBtn,row=4,column=0,pady=10)

GenPass=Button(generatorWidget,text="Generate Random Password",bg="grey",fg="white",command=ShowPass)
genSet.addWi(GenPass)
genSet.grid(GenPass,row=4,column=1,pady=10)

GoBack=genSet.addWi(Button(generatorWidget,text="GO Back !",bg="grey",fg="white"))
genSet.grid(GoBack,row=4,column=2,pady=10)



root.mainloop()
