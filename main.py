"""imported every class from the tkinter module"""
from tkinter import *

"""imported pandas module"""
import pandas

"""imported random module"""
import random


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


# ---------------------------- GENERATING RANDOM WORDS ------------------------------- #
"""variable to store the csv data"""
data = pandas.read_csv("data/french_words.csv")

"""converted to list of dictionaries"""
dataList = data.to_dict(orient="records")

"""variable to store the length of the dataList"""
dataListLength = len(dataList)

"""function to display random french words"""
def randomFrench():
    word = dataList[random.randint(0, dataListLength - 1)]["French"]
    canvas.itemconfig(wordText, text=word)


# ---------------------------- UI SETUP ------------------------------- #

# window

"""created the window object"""
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas

"""created the canvas object"""
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
cardFront = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=cardFront)
langText = canvas.create_text(400, 150, text="French", font=FONT_LANG, fill="black")
wordText = canvas.create_text(400, 263, text="trouve", font=FONT_WORD, fill="black")
canvas.grid(row=1, column=1, columnspan=2)

# button

"""created the buttonWrong object"""
wrongImage = PhotoImage(file="images/wrong.png")
buttonWrong = Button(image=wrongImage, bd=0, highlightthickness=0, command=randomFrench)
buttonWrong.grid(row=2, column=1)

"""created the buttonWrong object"""
rightImage = PhotoImage(file="images/right.png")
buttonWrong = Button(image=rightImage, bd=0, highlightthickness=0, command=randomFrench)
buttonWrong.grid(row=2, column=2)


"""loop to keep the window open"""
window.mainloop()
