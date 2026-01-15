from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# ----- WINDOW ----- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ----- CANVAS ----- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="FlashCard-Project/images/card_front.png")
card_back_img = PhotoImage(file="FlashCard-Project/images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="French")
# ----- BUTTONS ----- #
wrong_image = PhotoImage(file="FlashCard-Project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0)
correct_image = PhotoImage(file="FlashCard-Project/images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bd=0)
# ----- POSITIONS ----- #
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

window.mainloop()