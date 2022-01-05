from tkinter import *
from tkWinSwitch import *
from module import *
def Info():
    x=IDInput.get()
    y=PasswordInput.get()
    z=ConfpassInput.get()
    if y==z:
        addUser(x,y,conn)     

root=Tk()

SignUp= wiSet()

ID=Label(text="User ID")
SignUp.addWi(ID)
SignUp.grid(ID,row=0,column=0)

PassWord=Label(text="Password")
SignUp.addWi(PassWord)
SignUp.grid(PassWord,row=1,column=0)

ConfPassword=Label(text="Confirm Password")
SignUp.addWi(ConfPassword)
SignUp.grid(ConfPassword,row=2,column=0)


IDInput=Entry()
SignUp.addWi(IDInput)
SignUp.grid(IDInput,row=0,column=1)

PasswordInput=Entry()
SignUp.addWi(PasswordInput)
SignUp.grid(PasswordInput,row=1,column=1)

ConfpassInput=Entry()
SignUp.addWi(ConfpassInput)
SignUp.grid(ConfpassInput,row=2,column=1)

Signup_Bttn=Button(text="SignUp !",command=)
SignUp.addWi(Signup_Bttn)
SignUp.grid(Signup_Bttn,row=3, columnspan=2)


SignUp.create()

root.mainloop()