from tkinter import *

window = Tk()
window.title("Firt GUI")
window.minsize(width= 500, height= 300)
window.config(padx=10, pady=10)

def button_clicked():
    new_label.config(text=new_input.get())

# Labels
new_label = Label(text="I am a label", font=("Ariel", 24))

# Buttons
new_button = Button(text="Click Me", command=button_clicked)
test_button = Button(text="New Button")

# Entry
new_input =  Entry()

# Positions
new_label.grid(row=0, column=0)
new_button.grid(row=1, column=1)
test_button.grid(row=0, column=2)
new_input.grid(row=2, column= 3)

window.mainloop()