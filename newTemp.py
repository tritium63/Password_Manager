#importing modules
from abc import update_abstractmethods
from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from PIL import Image,ImageTk
from PIL import *
from module import *
from tkWinSwitch import *
from tkinter import messagebox

root=Tk()
#functions for buttons and other widgets
def SubmitFn():
    global MasterID
    MID=userentry.get()
    MPWD=passentry.get()
    print(MID, MPWD)
    if UserVerification(MID,MPWD,conn):
        switch(LoginPage,MenuPage)
        MasterID = MID
        uservalue.set('')
        passvalue.set('')
    else:
        print("Opps")        

def switchUpdate():
    switch(MenuPage,updateset)

#Login Sceen
#title
root.geometry("1200x700")
root.title("Password Manager - Login Page")

LoginPage = wiSet()
#setting background image
bgImage=Image.open("newBg - Password Manager.jpg") 
# bgImage=bgImage.resize((root.winfo_screenmmwidth(),root.winfo_screenmmheight()), Image.ANTIALIAS)
bgImageTk= ImageTk.PhotoImage(bgImage)
bgLabel = Label(image=bgImageTk)
LoginPage.addWi(bgLabel)
LoginPage.pack(bgLabel,fill=BOTH,expand=TRUE)

#login widget
loginLabel=LoginPage.addWi(Label(bgLabel,bg="grey"))
LoginPage.place(loginLabel,rely=0.5,relx=0.5,anchor=CENTER)

#variables for fonts used
usualfont_tuple=("sans serif",12,"bold")
headFont_tuple=("sans serif",16,"bold")

#Welcome Text 
welText=LoginPage.addWi(Label(loginLabel, text="Welcome To Password Manager", font =headFont_tuple, bg="grey",fg="white"))
LoginPage.grid(welText,row=0,column=1,columnspan=3)

#taking entries of username and password
username=LoginPage.addWi(Label(loginLabel, text="Username: ",font=usualfont_tuple,bg="grey",fg="white",pady=12,padx=12))
password=LoginPage.addWi(Label(loginLabel,text="Paswword: ",font=usualfont_tuple,bg="grey",fg="white"))
LoginPage.grid(username,row=1,column=0)
LoginPage.grid(password,row=2,column=0)

uservalue=StringVar()
passvalue=StringVar()

userentry=LoginPage.addWi(Entry(loginLabel, textvariable=uservalue,width=40 ))
passentry=LoginPage.addWi(Entry(loginLabel,textvariable=passvalue,width=40))
LoginPage.grid(userentry,row=1,column=1,padx=10)
LoginPage.grid(passentry,row=2,column=1,padx=10)



#Creating submit button
submitBtn=LoginPage.addWi(Button(loginLabel, bg="grey", text="LOGIN",fg="white",command=SubmitFn))
LoginPage.grid(submitBtn,row=3,column=1,pady=10)

signupText=Label(loginLabel,text="Don't have an account? Sign Up.",font=usualfont_tuple,bg="grey",fg="white")
LoginPage.addWi(signupText)
LoginPage.grid(signupText,row=4,column=1)
signbtn = Button(loginLabel,text="Sign Up",command=lambda :switch(LoginPage,SignUp),bg="grey",fg="white")
LoginPage.addWi(signbtn)
LoginPage.grid(signbtn,row=5,column=1,pady=5)
LoginPage.create()

#ending of login page

# menu page

def logout():
    global MasterID
    switch(MenuPage,LoginPage)
    MasterID = ""
MenuPage = wiSet()

#setting background
bgLabel = Label(image=bgImageTk)
MenuPage.addWi(bgLabel)
MenuPage.pack(bgLabel,fill=BOTH,expand=TRUE)

#login widget
greyLabel=MenuPage.addWi(Label(bgLabel,bg="grey"))
MenuPage.place(greyLabel,rely=0.5,relx=0.5,anchor=CENTER)

menuText=Label(greyLabel,text="What do you want to do?",font=headFont_tuple,fg="white",bg="grey")
MenuPage.addWi(menuText)
MenuPage.pack(menuText,pady=10,padx=50)



btn2 = MenuPage.addWi(Button(greyLabel,text="Retrieve Password",command = lambda :switch(MenuPage,Display),fg="white",bg="grey",font=usualfont_tuple))
btn3 = MenuPage.addWi(Button(greyLabel,text="Add Record", command=lambda :switch(MenuPage, genSet),fg="white",bg="grey",font=usualfont_tuple))
btn4=MenuPage.addWi(Button(greyLabel,text="Update Existing Password",fg="white",bg="grey",font=usualfont_tuple,command=switchUpdate))
btn5=MenuPage.addWi(Button(greyLabel,text="Delete Existing Record",fg="white",bg="grey",font=usualfont_tuple,command=lambda:switch(MenuPage,delSet)))
btn1 = MenuPage.addWi(Button(greyLabel,text="Logout",command=logout,fg="white",bg="grey",font=usualfont_tuple))

MenuPage.pack(btn2,pady=10)
MenuPage.pack(btn1,pady=10)
MenuPage.pack(btn4,pady=10)
MenuPage.pack(btn5,pady=10)
MenuPage.pack(btn3,pady=10)
#ending of menu page

#display pass screen
Display=wiSet()

#setting background
bgLabel = Label(image=bgImageTk)
Display.addWi(bgLabel)
Display.pack(bgLabel,fill=BOTH,expand=TRUE)

centLabel=Display.addWi(Label(bgLabel,bg="grey"))
Display.place(centLabel,rely=0.5,relx=0.5,anchor=CENTER)

ListBoxLabel=Label(centLabel,text="Login Info",font=("sans serif",16,BOLD),fg="white",bg="grey")
ListBox=Listbox(centLabel,height = 10, width = 50, bg = "grey", activestyle = 'dotbox')

sBox = StringVar()
searchBoxText=Label(centLabel,text="Enter Service Name:",font=usualfont_tuple,fg="white",bg="grey")
SearchBox=Entry(centLabel,text="Enter Service Name",textvariable=sBox,width=30)


Search=Button(centLabel,text="Search", command= lambda : ShowServiceOut(),fg="white",bg="grey")
Exit=Button(centLabel,text="Go Back", command= lambda : Exit(),fg="white",bg="grey")


Display.addWi(ListBoxLabel)
Display.addWi(ListBox)
Display.addWi(searchBoxText)
Display.addWi(SearchBox)
Display.addWi(Search)
Display.addWi(Exit)


Display.pack(ListBoxLabel)
Display.pack(ListBox)
Display.pack(searchBoxText,pady=20)
Display.pack(SearchBox)
Display.pack(Search,pady=20)
Display.pack(Exit,pady=10)


def Exit():
    ListBox.delete(0,END)
    sBox.set('')
    switch(Display,MenuPage)
    


def ShowServiceOut():
    ListBox.delete(0,END)
    Service=SearchBox.get()
    ServiceOut=Searching(Service, MasterID, con=conn)
    if ServiceOut != False:
        
        N=0
        for i in ServiceOut:
            ListBox.insert(N,f"{i}")
            N+=1
    else:
        pass
    if not ServiceOut:
        ListBox.insert(0,"no result found")

def ShowPass(v):
    v.set(PassGen())


def passvals():
    TempPass=PasswordEntry.get()
    TempService=serviceNameval.get()
    UIDD=userIDval.get()
    if TempService=="" or UIDD=="" or TempPass=="":
        messagebox.showerror("Invalid Input", "Fields Cannot be Empty")
    else:
        addData(MasterID,TempService, UIDD, TempPass, conn)
        Pass.set("")
        UVar.set("")
        SVar.set("")

#creating set for generator page 
genSet=wiSet()

#fonts
headfont_tuple=("sans serif",16,"bold")
generalFont=("sans serif",12,"bold")

#setting background
bgLabel = Label(image=bgImageTk)
genSet.addWi(bgLabel)
genSet.pack(bgLabel,fill=BOTH,expand=TRUE)



generatorWidget=Label(bgLabel,bg="grey")
# generatorWidget.place(relx=0.5,rely=0.5,anchor=CENTER)                    
genSet.addWi(generatorWidget)
genSet.place(generatorWidget, relx=0.5,rely=0.5, anchor=CENTER)
# Heading Text
headText=Label(generatorWidget,text="New UID and Password Generation", font=headfont_tuple,bg="grey",fg="white",padx=30)
# headText.grid(row=0,column=1)
genSet.addWi(headText)
genSet.grid(headText,row=0,column=1)

# #entry fields
userID=Label(generatorWidget,text="User ID:",font=generalFont,bg="grey",fg="white",pady=10)
# userID.grid(row=1,column=0)
genSet.addWi(userID)
genSet.grid(userID,row=1,column=0)


passWord=Label(generatorWidget,text="Password:",font=generalFont,bg="grey",fg="white")
# passWord.grid(row=2,column=0)
genSet.addWi(passWord)
genSet.grid(passWord,row=2,column=0)

Pass=StringVar()

PasswordEntry=Entry(generatorWidget, width=75, textvariable=Pass)
genSet.addWi(PasswordEntry)
genSet.grid(PasswordEntry,row=2,column=1,columnspan=2)


serviceName=Label(generatorWidget,text="Service Name:",font=generalFont,bg="grey",fg="white",pady=10)
# serviceName.grid(row=3,column=0)
genSet.addWi(serviceName)
genSet.grid(serviceName,row=3,column=0)

UVar=StringVar()
userIDval=Entry(generatorWidget,width=75, textvariable=UVar)
# userIDval.grid(row=1,column=1)
genSet.addWi(userIDval)
genSet.grid(userIDval,row=1,column=1,columnspan=2)
SVar=StringVar()
serviceNameval=Entry(generatorWidget,width=75, textvariable=SVar)
# serviceNameval.grid(row=3,column=1)
genSet.addWi(serviceNameval)
genSet.grid(serviceNameval,row=3,column=1,columnspan=2)
#submit button
submitBtn=Button(generatorWidget,text="Submit",bg="grey",fg="white",command=passvals)
# submitBtn.grid(row=4,column=1,pady=10)
genSet.addWi(submitBtn)
genSet.grid(submitBtn,row=4,column=0,pady=10)

GenPass=Button(generatorWidget,text="Generate Random Password",bg="grey",fg="white",command=lambda:ShowPass(Pass))
genSet.addWi(GenPass)
genSet.grid(GenPass,row=4,column=1,pady=10)


def GenSetBack():
    Pass.set("")
    UVar.set("")
    SVar.set("")
    switch(genSet, MenuPage)

GoBack=genSet.addWi(Button(generatorWidget,text="GO Back !",bg="grey",fg="white",command=GenSetBack))
genSet.grid(GoBack,row=4,column=2,pady=10)

def Info():
    x=IDInput.get()
    y=PasswordInput.get()
    z=ConfpassInput.get()
    if x=="" or y == "" or z == "":
        messagebox.showerror("Error","Field can not be empty")
    else:

        try:
            if len(y)>32 or len(x)>32:
                messagebox.showerror("error","Please enter values less than 32 character")
            else:
                if y==z:
                    status = addUser(x,y,conn)
                    if status==1:
                        messagebox.showerror("User alredy exist","Sorry the username is alredy in use,\nPlease try a different one.")    
                else:
                    messagebox.showerror("Error","Password does not match")    
        except Exception as e:
            print(e)
            messagebox.showerror("Error","some error occured")

#sign up screen
SignUp= wiSet()

#setting background
bgLabel = Label(image=bgImageTk)
SignUp.addWi(bgLabel)
SignUp.pack(bgLabel,fill=BOTH,expand=TRUE)

signLabel=SignUp.addWi(Label(bgLabel,bg="grey"))
SignUp.place(signLabel,rely=0.5,relx=0.5,anchor=CENTER)

ID=Label(signLabel,text="User ID:",font=usualfont_tuple,fg="white",bg="grey")
SignUp.addWi(ID)
SignUp.grid(ID,row=0,column=0)

PassWord=Label(signLabel,text="Password:",font=usualfont_tuple,fg="white",bg="grey")
SignUp.addWi(PassWord)
SignUp.grid(PassWord,row=1,column=0)

ConfPassword=Label(signLabel,text="Confirm Password:",font=usualfont_tuple,fg="white",bg="grey")
SignUp.addWi(ConfPassword)
SignUp.grid(ConfPassword,row=2,column=0)

s1 = StringVar()
IDInput=Entry(signLabel,textvariable=s1)
SignUp.addWi(IDInput)
SignUp.grid(IDInput,row=0,column=1)

s2=StringVar()
PasswordInput=Entry(signLabel,textvariable=s2)
SignUp.addWi(PasswordInput)
SignUp.grid(PasswordInput,row=1,column=1)

s3=StringVar()
ConfpassInput=Entry(signLabel,textvariable=s3)
SignUp.addWi(ConfpassInput)
SignUp.grid(ConfpassInput,row=2,column=1,padx=10)

Signup_Bttn=Button(signLabel,text="Sign Up",command=Info,fg="white",bg="grey")
SignUp.addWi(Signup_Bttn)
SignUp.grid(Signup_Bttn,row=3, columnspan=2,pady=10)

def sgGo():
    s1.set("")
    s2.set("")
    s3.set("")
    switch(SignUp,LoginPage)

signBack=Button(signLabel,text="Go Back",command=lambda :sgGo(),fg="white",bg="grey")
SignUp.addWi(signBack)
SignUp.grid(signBack,row=4, columnspan=2,pady=10)


#updation screen
#fn definition
def UpdatePass():
    userId=askUserVal.get()
    service=askServiceVal.get()
    newPass=newPassVal.get()
    print(MasterID,userId,service,newPass)
    Update(MasterID,userId,service,newPass,conn)

    



#initial
updateset=wiSet()

#setting background
bgLabel = Label(image=bgImageTk)
updateset.addWi(bgLabel)
updateset.pack(bgLabel,fill=BOTH,expand=TRUE)

greyBg=updateset.addWi(Label(bgLabel,bg="grey"))
updateset.place(greyBg,rely=0.5,relx=0.5,anchor=CENTER)
greyBg=updateset.addWi(Label(bgLabel,bg="grey"))
updateset.place(greyBg,rely=0.5,relx=0.5,anchor=CENTER)

#heading text
headingText=updateset.addWi(Label(greyBg,text="Updating Password",font=headfont_tuple,fg="white",bg="grey"))
updateset.grid(headingText,row=0,column=0,padx=200)
#entry fields
askService=updateset.addWi(Label(greyBg,text="Enter Service to change Password for:",font=usualfont_tuple,fg="white",bg="grey"))
updateset.grid(askService,row=1,column=0,pady=20)

askServiceVal=updateset.addWi(Entry(greyBg,width=30))
updateset.grid(askServiceVal,row=2,column=0)

askUser=updateset.addWi(Label(greyBg,text="Enter User ID to confirm",font=usualfont_tuple,bg="grey",fg="white"))
updateset.grid(askUser,row=3,column=0,pady=20)

askUserVal=updateset.addWi(Entry(greyBg,width=30))
updateset.grid(askUserVal,row=4,column=0)



newPass=updateset.addWi(Label(greyBg,text="New Password:",font=usualfont_tuple,fg="white",bg="grey"))
updateset.grid(newPass,row=5,column=0,pady=5)

# newPassVal=updateset.addWi(Entry(greyBg,width=30))
# updateset.grid(newPassVal,row=6,column=0,pady=20)

# passWordLabel=Label(greyBg,text="Password:",font=generalFont,bg="grey",fg="white")
# # passWord.grid(row=2,column=0)
# updateset.addWi(passWordLabel)
# updateset.grid(passWordLabel,row=2,column=0)

Pass=StringVar()

upPass=StringVar()
newPassVal=Entry(greyBg, width=30, textvariable=upPass)
updateset.addWi(newPassVal)
updateset.grid(newPassVal,row=6,column=0)


#submit button
SubmitBtn=updateset.addWi(Button(greyBg, bg="grey", text="Submit",fg="white",command=UpdatePass))
updateset.grid(SubmitBtn,row=7,column=0,pady=10)
#genPassButton

GenPassBtn=Button(greyBg,text="Generate Random Password",bg="grey",fg="white",command=lambda:ShowPass(upPass))
updateset.addWi(GenPassBtn)
updateset.grid(GenPassBtn,row=8,column=0,pady=10)

#BACK BUTTON
GoBackBtn=updateset.addWi(Button(greyBg,text="GO Back !",bg="grey",fg="white",command=lambda: switch(updateset,MenuPage)))
updateset.grid(GoBackBtn,row=9,column=0,pady=10)


##Deletion screen
#defining function
def deleteRec():
    username=userAccVal.get()
    delrecord(MasterID,username,conn)

#initializing
delSet=wiSet()
def passval():
    print("rec deleted")

#setting background
bgLabel = Label(image=bgImageTk)
delSet.addWi(bgLabel)
delSet.pack(bgLabel,fill=BOTH,expand=TRUE)

#grey layout
greyBg=delSet.addWi(Label(bgLabel,bg="grey"))
delSet.place(greyBg,rely=0.5,relx=0.5,anchor=CENTER)

#Heading
intitialText=delSet.addWi(Label(greyBg,text="Delete Record Here",font=("Comic Sans MS",16,BOLD),bg="grey",fg="white",width=50,height=100))
delSet.place(intitialText,relx=0.5,rely=0.1,anchor=CENTER)

#entry fields
# servName=delSet.addWi(Label(greyBg,text="Enter Service Name: ",font=usualfont_tuple,bg="grey",fg="white"))
# delSet.grid(servName,row=1,column=0,pady=(50,10))
# servNameVal=delSet.addWi(Entry(greyBg,width=65))
# delSet.grid(servNameVal,row=1,column=2,pady=(50,10),padx=(0,10))

userAcc=delSet.addWi(Label(greyBg,text="Enter User ID:",font=usualfont_tuple,fg="white",bg="grey"))
delSet.grid(userAcc,row=2,column=0,pady=(40,10))
userAccVal=delSet.addWi(Entry(greyBg,width=65))
delSet.grid(userAccVal,row=2,column=2,pady=(40,10),padx=(0,10))

##just in case for need of password
# wordPass=delSet.addWi(Label(greyBg,text="Enter Password to confirm:",font=usualfont_tuple,fg="white",bg="grey"))
# delSet.grid(wordPass,row=3,column=0,pady=10,padx=(10,0))
# wordPassVal=delSet.addWi(Entry(greyBg,width=65))
# delSet.grid(wordPassVal,row=3,column=2,pady=10,padx=(0,10))

DelBtn=delSet.addWi(Button(greyBg,text="Delete Record",fg="white",bg="grey",command=deleteRec))
delSet.grid(DelBtn,row=4,column=2,pady=10)

#BACK BUTTON
BackBtn=delSet.addWi(Button(greyBg,text="GO Back",bg="grey",fg="white",command=lambda: switch(delSet,MenuPage)))
delSet.grid(BackBtn,row=4,column=0,pady=10)

root.mainloop()
