"""imported every class from the tkinter module"""
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Ariel", 40, "italic")
FONT_WORD = ("Ariel", 60, "bold")


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
buttonWrong = Button(image=wrongImage, bd=0, highlightthickness=0)
buttonWrong.grid(row=2, column=1)

"""created the buttonWrong object"""
rightImage = PhotoImage(file="images/right.png")
buttonWrong = Button(image=rightImage, bd=0, highlightthickness=0)
buttonWrong.grid(row=2, column=2)


"""loop to keep the window open"""
window.mainloop()
