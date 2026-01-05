from tkinter import *

window = Tk()
window.title("Firt GUI")
window.minsize(width= 500, height= 300)

def button_clicked():
    new_label.config(text=new_input.get())

# Labels
new_label = Label(text="I am a label", font=("Ariel", 24))

# Buttons
new_button = Button(text="Click Me", command=button_clicked)

# Entry
new_input =  Entry()

# Positions
new_label.pack()
new_button.pack()
new_input.pack()

window.mainloop()