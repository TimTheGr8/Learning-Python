from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass
# ---------------------------- UI SETUP ------------------------------- #
# ----- WINDOW ----- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# ----- CANVAS ----- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="Password-Manager/logo.png")
canvas.create_image(100, 100, image=lock_img)
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
add_button = Button(text="Add", command=save_password, width=36)
# ----- POSITIONS ----- #
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
password_label.grid(row=3, column=0)
password_enrty.grid(row=3, column=1, sticky="EW")
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")


window.mainloop()