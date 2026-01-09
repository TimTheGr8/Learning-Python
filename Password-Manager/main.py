from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# TODO: Fix this to search and overwrite the websites already in the file

# ----- PASSWORD GEN VARIABLES ----- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_enrty.delete(0, END)
    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password ="".join(password_list)
    password_enrty.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def confirm_save():
    site = website_entry.get()
    user = username_entry.get()
    pword = password_enrty.get()
    if len(user) == 0 or len(pword) == 0 or len(user) == 0:
        messagebox.showerror(title="ERROR", message="Some fields were left blank. Please fill out all fields before continuing.")
    else:
        continue_saving = messagebox.askokcancel(title=site, message=f"These are the details entered:\nEmail: {user}\nPassword: {pword}\nContinue saving?")
        if continue_saving:
            save_password(site, user, pword)

def save_password(website, email, password): 
    with open("Password-Manager/data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
    messagebox.showinfo(title="Success", message="Username and password have been saved!!!!")
    clear_fields()

def clear_fields():
    website_entry.delete(0, END)
    password_enrty.delete(0, END)
    website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
# ----- WINDOW ----- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# ----- CANVAS ----- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="Password-Manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
# ----- WIDGETS ----- #
# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
# Entries
website_entry = Entry(width=35)
username_entry = Entry(width=35)
password_enrty = Entry(width=21)
#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=confirm_save, width=36)
# ----- POSITIONS ----- #
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0,"tjanssen4@gmail.com")
password_label.grid(row=3, column=0)
password_enrty.grid(row=3, column=1, sticky="EW")
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()