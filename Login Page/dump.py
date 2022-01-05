
bgImage=Image.open("Background Design - Password Manager.jpg") 
bgImageTk= ImageTk.PhotoImage(bgImage)
bgLabel = Label(image=bgImageTk)
bgLabel.pack(fill=X)

loginLabel=Label(bgLabel,bg="red")
loginLabel.pack()

#taking entries of username and password
username=Label(loginLabel, text="Username: ")
password=Label(loginLabel,text="Paswword: ")
username.pack()
password.pack()

#Creating submit button
submitBtn=Button(bgLabel, bg="white", text="Submit")
submitBtn.pack()