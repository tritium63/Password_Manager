#importing modules 
from tkinter import *
from PIL import Image,ImageTk



root=Tk()
root.geometry("1200x700")
root.title("Password Manger - Menu")
#creating set widget
# menuSet=wiSet()
#fonts
headfont_tuple=("Comic Sans MS",16,"bold")
generalFont=("Comic Sans MS",12,"bold")

#setting background
bgImage=Image.open("Background Design - Password Manager.jpg")
bgImageTk=ImageTk.PhotoImage(bgImage)
bgLabel=Label(image=bgImageTk)
bgLabel.pack(fill=BOTH,expand=TRUE)
# menuSet.addWi(bgLabel)
# menuSet.pack(bgLabel,fill=BOTH,expand=TRUE)


menuWidget=Label(bgLabel,bg="black")
menuWidget.place(relx=0.5,rely=0.5,anchor=CENTER)

# menuSet.addWi(menuWidget)
# menuSet.place(menuWidget,relx=0.5,rely=0.5,anchor=CENTER)
promptlabel=Label(menuWidget,text="What do you want to do?",bg="black",fg="white",font=generalFont)
promptlabel.place(relx=0.25)

#generate password for new service 
genBtn=Button(menuWidget, text="Generate New Password",bg="grey",fg="white")
genBtn.grid(padx=20,pady=40)


#access existing records
checkBtn=Button(menuWidget,text="Access Existing Records",bg="grey",fg="white")
checkBtn.grid(row=0,column=1,padx=20,pady=40)


root.mainloop()
