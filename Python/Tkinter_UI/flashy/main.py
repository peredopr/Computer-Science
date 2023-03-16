from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
    

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    current_word = current_card["French"]
    canvas.itemconfig(title_canvas, text="French")
    canvas.itemconfig(word_canvas, text=current_word)
    canvas.itemconfig(card_backgroud, image=card_front_image)
    timer = window.after(3000, func=flip_card)

def known_cards():
    data_dict.remove(current_card)
    next_card()
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

def flip_card():
    canvas.itemconfig(title_canvas, text="English")
    canvas.itemconfig(word_canvas, text=current_card["English"])
    canvas.itemconfig(card_backgroud, image=card_back_image)

window = Tk()
window.title("Flashy")
window.config(padx=40, pady=20, background=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)


#Canvas Image
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_backgroud = canvas.create_image(400, 265, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

#Canvas Text
title_canvas = canvas.create_text(380, 150, text="", font=("Ariel",30,"italic"))
word_canvas = canvas.create_text(380, 263, text="", font=("Ariel",50,"bold"))




wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

#Labels

#Buttons
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=known_cards)
wrong_button.grid(column=1, row=1)


next_card()

window.mainloop()