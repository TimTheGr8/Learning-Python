from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def calculate():
    result = float(mile_entry.get()) * 1.609
    conversion_label.config(text=f"{result:.2f}")
    mile_entry.focus()

#////////// WIDGETS \\\\\\\\\\
# Entries
mile_entry = Entry(width=8)
# Lables
mile_label = Label(text="Miles")
equal_label = Label(text="is equal to ")
conversion_label = Label(text="0")
km_label = Label(text="Km")
# Buttons
calculate_button = Button(text="Calculate", command=calculate)

# Locations
mile_entry.grid(row=0, column=1)
mile_label.grid(row=0, column=2)
equal_label.grid(row=1, column=0)
conversion_label.grid(row=1, column=1)
km_label.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)

mile_entry.focus()


window.mainloop()