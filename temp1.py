#importing modules
from tkinter import *
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
usualfont_tuple=("Comic Sans MS",12,"bold")
headFont_tuple=("Comic Sans MS",16,"bold")

#Welcome Text 
welText=LoginPage.addWi(Label(loginLabel, text="Welcome To Password Manager", font =headFont_tuple, bg="grey",fg="white"))
LoginPage.grid(welText,row=0,column=1)

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
btn1 = MenuPage.addWi(Button(greyLabel,text="Logout",command=logout,fg="white",bg="grey",font=usualfont_tuple))

MenuPage.pack(btn2,pady=10)
MenuPage.pack(btn1,pady=10)
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

ListBoxLabel=Label(centLabel,text="Login Info",font=("Comic Sans MS",16,BOLD),fg="white",bg="grey")
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
        Pass.set("")
        UVar.set("")
        SVar.set("")

#creating set for generator page 
genSet=wiSet()

#fonts
headfont_tuple=("Comic Sans MS",16,"bold")
generalFont=("Comic Sans MS",12,"bold")

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

GenPass=Button(generatorWidget,text="Generate Random Password",bg="grey",fg="white",command=ShowPass)
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
                    messagebox.showerror("User alredy exit","Sorry the username is alredy in use,\nPlese try a different one.")
        except:
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

root.mainloop()
