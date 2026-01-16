from tkinter import *
import pandas as pd
import random
import pygame
# ---------------------------- VARIABLES ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
audio_file = "FlashCard-Project/audio/"

try:
    data = pd.read_csv("FlashCard-Project/data/to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("FlashCard-Project/data/morse_code.csv")

to_learn = data.to_dict(orient="records")
pygame.mixer.init()
# ---------------------------- NEW WORD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_card, image=card_front_img)
    canvas.itemconfig(title_text, text="Morse", fill="black")
    canvas.itemconfig(letter_text, text=current_card["Morse"], fill="black")
    letter_sound = pygame.mixer.Sound(f"{audio_file}{current_card['Letter'].lower()}.wav")
    letter_sound.play()
    flip_timer = window.after(3000, flip_card)
# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(canvas_card, image=card_back_img)
    canvas.itemconfig(title_text, text="Alphabet", fill="white")
    canvas.itemconfig(letter_text, text=current_card["Letter"], fill="white")
# ---------------------------- REMOVE WORD ------------------------------- #
def remove_word():
    global current_card
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("FlashCard-Project/data/to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
# ----- WINDOW ----- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
# ----- CANVAS ----- #
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="FlashCard-Project/images/card_front.png")
card_back_img = PhotoImage(file="FlashCard-Project/images/card_back.png")
canvas_card = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
letter_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
# ----- BUTTONS ----- #
wrong_image = PhotoImage(file="FlashCard-Project/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=next_card)
correct_image = PhotoImage(file="FlashCard-Project/images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bd=0, command=remove_word)
# ----- POSITIONS ----- #
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
correct_button.grid(row=1, column=1)

next_card()
window.mainloop()