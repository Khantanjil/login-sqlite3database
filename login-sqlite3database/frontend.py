from tkinter import *
from tkinter import font
from backend import Database

# Function

database = Database("account.db")

def login_account():
    list = [username_entry_text.get(), password_entry_text.get()]
    if len(list[0]) < 1 or len(list[1]) < 1:
        blank.config(text="Fill the credentials.", font=myFont)
    else:
        database.insert(
            username_entry_text.get(),
            password_entry_text.get()
        )
        blank.config(text="Logged in!", font=myFont)
        print(database.view())


window = Tk()
window.wm_title("Login")
window.geometry("500x100")

myFont = font.Font(family="Helvetica", size=10)


# Interface
blank = Label(window, text="")
blank.grid(row=0, column=0)

username = Label(window, text="Username", font=myFont)
username.grid(row=1, column=0)
username_entry_text = StringVar()
username_entry = Entry(
    window, textvariable=username_entry_text, width=25, font=myFont)
username_entry.grid(row=1, column=1)

password = Label(window, text="Password", font=myFont)
password.grid(row=2, column=0)
password_entry_text = StringVar()
password_entry = Entry(
    window, textvariable=password_entry_text, width=25, font=myFont, show="*")
password_entry.grid(row=2, column=1)

login = Button(window, text="Login", font=myFont, command=login_account)
login.grid(row=3, column=1)

window.mainloop()
