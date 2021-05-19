import random

from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}

# ------------------------------READING DATA------------------------#
try:
    word_data = pandas.read_csv("data/words_to_lean.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = word_data.to_dict(orient="records")


# ------------------------------RANDOM WORD------------------------#
current_card = {}
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language_name, text="French", fill="green")
    canvas.itemconfig(word, text=current_card["French"], fill="purple")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip)
# ------------------------------FLIP------------------------#
def flip():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(language_name, text="English", fill="magenta")
    canvas.itemconfig(word, text=current_card["English"], fill="magenta")

# ------------------------------SAVING PROGRESS------------------------#
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ------------------------------UI SETUP----------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_name = canvas.create_text(400, 150, text="", fill="orange", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="brown", font=("Arial", 60, "bold"))
canvas.grid(column=0, columnspan=2, row=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)

next_card()

window.mainloop()
