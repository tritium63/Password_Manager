from tkinter import *


top = Tk()
top.geometry("450x300")
	

user_name = Label(top, text = "Username").place(x = 40, y = 60)
user_password = Label(top, text = "Password").place(x = 40, y = 100)
submit_button = Button(top, text = "Submit").place(x = 40, y = 130)
user_name_input_area = Entry(top, width = 30).place(x = 110, y = 60)
user_password_entry_area = Entry(top, width = 30).place(x = 110, y = 100)
	
top.mainloop()

