#importing modules 
from tkinter import *
from PIL import Image,ImageTk
from tkWinSwitch import *

root=Tk()
root.geometry("1200x700")
root.title("Password Manager - Password Generator")
#functions
def passvals():
    pass

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
userID=Label(generatorWidget,text="User ID:",font=generalFont,bg="black",fg="white",pady=20)
# userID.grid(row=1,column=0)
genSet.addWi(userID)
genSet.grid(userID,row=1,column=0)


passWord=Label(generatorWidget,text="Generated Password:",font=generalFont,bg="black",fg="white")
# passWord.grid(row=2,column=0)
genSet.addWi(passWord)
genSet.grid(passWord,row=2,column=0)

serviceName=Label(generatorWidget,text="Service Name:",font=generalFont,bg="black",fg="white",pady=10)
# serviceName.grid(row=3,column=0)
genSet.addWi(serviceName)
genSet.grid(serviceName,row=3,column=0)


userIDval=Entry(generatorWidget,width=50)
# userIDval.grid(row=1,column=1)
genSet.addWi(userIDval)
genSet.grid(userIDval,row=1,column=1)

serviceNameval=Entry(generatorWidget,width=50)
# serviceNameval.grid(row=3,column=1)
genSet.addWi(serviceNameval)
genSet.grid(serviceNameval,row=3,column=1)
#submit button
submitBtn=Button(generatorWidget,text="Submit",bg="grey",fg="white",command=passvals)
# submitBtn.grid(row=4,column=1,pady=10)
genSet.addWi(submitBtn)
genSet.grid(submitBtn,row=4,column=1,pady=10)

#setting initial screen
genSet.create()

root.mainloop()
