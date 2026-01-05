from tkinter import *
import time
# TODO: Get the window to pop to the top when current timer is done.
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25 # 25
SHORT_BREAK_MIN = 0.15 # 5
LONG_BREAK_MIN = 0.5 # 20
BLANK_CHECKMARK = "☐ "
FILLED_CHECKMARK = "☑ "

timer = None
reps = 0
competed_checkmarks = [BLANK_CHECKMARK, BLANK_CHECKMARK, BLANK_CHECKMARK, BLANK_CHECKMARK]

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global competed_checkmarks
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=time.strftime("%M:%S", time.gmtime(0)))
    competed_checkmarks = [BLANK_CHECKMARK, BLANK_CHECKMARK, BLANK_CHECKMARK, BLANK_CHECKMARK]
    checkmark_label.config(text=("".join(competed_checkmarks)))
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    count = 0
    reps += 1
    if reps == 8:
        count = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
    else:
        count = WORK_MIN * 60
        timer_label.config(text="Work", fg=GREEN)

    countdown(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    canvas.itemconfig(timer_text, text=time.strftime("%M:%S", time.gmtime(count)))
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            competed_checkmarks[int(reps / 2) - 1] = FILLED_CHECKMARK
            checkmark_label.config(text=("".join(competed_checkmarks)))

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro-App/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# Labels
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
checkmark_label = Label(text=("".join(competed_checkmarks)), fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
#Buttons
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)

# ----- POSITIONS ----- #
timer_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
checkmark_label.grid(row=3,column=1)

window.mainloop()