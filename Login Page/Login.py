#importing modules
from os import terminal_size
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
# from module import *
from tkWinSwitch import *


root=Tk()
#functions for buttons and other widgets
def SubmitFn():
    pass
# def SubmitFn():
#     MID=userentry.get()
#     MPWD=passentry.get()
#     print(MID, MPWD)
#     if UserVerification(MID,MPWD,conn):
#         print("Woho")
#     else:
#         print("Opps")        



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
submitBtn=set1.addWi(Button(loginLabel, bg="grey", text="Submit",fg="white",command=SubmitFn))
set1.grid(submitBtn,row=3,column=1)

set1.create()
root.mainloop()
