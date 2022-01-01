#importing modules
from os import terminal_size
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from module import *



root=Tk()
#functions for buttons and other widgets
def SubmitFn():
    MID=userentry.get()
    MPWD=passentry.get()
    print(MID, MPWD)
    if UserVerification(MID,MPWD,conn):
        print("Login Sucessfull")
    else:
        print("Login Unsucessfull")        



#title
root.geometry("1200x700")
root.title("Password Manager - Login Page")

#setting background image
bgImage=Image.open("Background Design - Password Manager.jpg") 
bgImageTk= ImageTk.PhotoImage(bgImage)
bgLabel = Label(image=bgImageTk)
bgLabel.pack(fill=BOTH,expand=YES)

#login widget
loginLabel=Label(bgLabel,bg="black")
loginLabel.place(rely=0.5,relx=0.5,anchor=CENTER)

#variables for fonts used
usualfont_tuple=("Comic Sans MS",12,"bold")
headFont_tuple=("Comic Sans MS",16,"bold")

#Welcome Text 
welText=Label(loginLabel, text="Welcome To Password Manager", font =headFont_tuple, bg="black",fg="white")
welText.grid(row=0,column=1)

#taking entries of username and password
username=Label(loginLabel, text="Username: ",font=usualfont_tuple,bg="black",fg="white",pady=12,padx=12)
password=Label(loginLabel,text="Paswword: ",font=usualfont_tuple,bg="black",fg="white")
username.grid(row=1,column=0)
password.grid(row=2,column=0)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(loginLabel, textvariable=uservalue,width=40 )
passentry=Entry(loginLabel,textvariable=passvalue,width=40)
userentry.grid(row=1,column=1,padx=10)
passentry.grid(row=2,column=1,padx=10)




#Creating submit button
submitBtn=Button(loginLabel, bg="grey", text="Submit",fg="white",command=SubmitFn)


root.mainloop()
