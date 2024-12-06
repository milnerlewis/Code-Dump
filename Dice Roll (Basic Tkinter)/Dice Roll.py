from tkinter import *
import random

def rollButtonClick():
    diceRollOne = random.randint(1,6)
    displayBox.delete(0, "end")
    displayBox.insert(0, diceRollOne)

window = Tk()
window.geometry("300x200")

window.configure(bg='blue')

title = Label(window, text="Dice Roller")
rollButton = Button(window, text="Press to roll", command = rollButtonClick)
displayBox = Entry(window)

title.pack()
rollButton.pack()
displayBox.pack()

window.mainloop()