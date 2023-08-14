from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# read the CSV data passed through
try:
    words_data = pandas.read_csv("./data/words_to_learn.csv")
    print("Nope")
except FileNotFoundError:
    words_data = pandas.read_csv("./data/french_words.csv")
    to_learn = words_data.to_dict(orient="records")
    current_card = {}
    print("Yep")
else:
    to_learn = words_data.to_dict(orient="records")
    current_card = {}


def create_current_card():
    global current_card
    current_card = random.choice(to_learn)
    selected_language = list(current_card.keys())[0]
    word_in_language = current_card["French"]
    canvas.itemconfig(card_word, text=f"{word_in_language}", fill="black")
    canvas.itemconfig(card_title, text=f"{selected_language}", fill="black")
    canvas.itemconfig(instructions, text="Select the 'Green Checkmark' if you got it right or the 'Red Checkmark' "
                                         "to review the word later", anchor="center", font=("Ariel", 10, "italic"),
                      fill="black")
    canvas.itemconfig(card_background, image=front_image)


def next_card_correct():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    create_current_card()


def flip_card():
    english_language = list(current_card.keys())[1]
    word_in_language = current_card["English"]
    canvas.itemconfig(card_word, text=f"{word_in_language}", fill="white")
    canvas.itemconfig(card_title, text=f"{english_language}", fill="white")
    canvas.itemconfig(instructions, text="Select the 'Green Checkmark' if you got it right or the 'Red Checkmark' "
                                         "to review the word later", anchor="center", font=("Ariel", 10, "italic"),
                      fill="white")
    canvas.itemconfig(card_background, image=back_image)


# Set up the window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=900, height=626)

# Creating the background of the Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

# Creating the front image
front_image = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 275, image=front_image)
instructions = canvas.create_text(400, 50, text="Select the 'Green Checkmark' if you got it right or the 'Red"
                                                " Checkmark' to review the word later", anchor="center",
                                                font=("Ariel", 10, "italic"), fill="black")
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, columnspan=3)

# Creating the back image
back_image = PhotoImage(file="./images/card_back.png")

# Creating the correct image button
correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, command=next_card_correct, highlightthickness=0)
correct_button.grid(column=0, row=1)

# Creating the wrong image button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=create_current_card, highlightthickness=0)
wrong_button.grid(column=2, row=1)

check_answer = Button(text="Reveal Answer", command=flip_card, highlightthickness=0)
check_answer.grid(column=1, row=1)

create_current_card()

window.mainloop()
