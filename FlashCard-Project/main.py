from tkinter import *
import pandas as pd
import random
# ---------------------------- VARIABLES ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

word_df = pd.read_csv("FlashCard-Project/data/french_words.csv")
to_learn = word_df.to_dict(orient="records")
# ---------------------------- NEW WORD ------------------------------- #
def next_card():
    current_card = random.choice(to_learn)
    language = "French"
    new_word = current_card["French"]
    canvas.itemconfig(language_text, text=language)
    canvas.itemconfig(word_text, text=new_word)
# ---------------------------- UI SETUP ------------------------------- #
# ----- WINDOW ----- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ----- CANVAS ----- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="FlashCard-Project/images/card_front.png")
card_back_img = PhotoImage(file="FlashCard-Project/images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
# ----- BUTTONS ----- #
wrong_image = PhotoImage(file="FlashCard-Project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
correct_image = PhotoImage(file="FlashCard-Project/images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bd=0, command=next_card)
# ----- POSITIONS ----- #
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

next_card()
window.mainloop()