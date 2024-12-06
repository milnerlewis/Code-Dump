from tkinter import *
import random

maxNumber = 2

def randomNumberGenerate():
    randomNumber = random.randint(1,maxValueBox)
    displayBox.delete(0, "end")
    displayBox.insert(0, randomNumber)

def maxValueIncrease():
    global maxNumber
    newMaxNumber = maxNumber + 1
    maxNumber = newMaxNumber
    maxValueBox.delete(0, "end")
    maxValueBox.insert(0, newMaxNumber)

def maxValueDecrease():
    global maxNumber
    newMaxNumber = maxNumber - 1
    maxNumber = newMaxNumber
    maxValueBox.delete(0, "end")
    maxValueBox.insert(0, newMaxNumber)


window = Tk()
window.geometry("300x200")

window.configure(bg='blue')

title = Label(window, text="Random number generator")
increaseButton = Button(window, text="Press to increase max number", command = maxValueIncrease)
maxValueBox = Entry(window, text=maxNumber)
maxValueBox.insert(0, maxNumber)
decreaseButton = Button(window, text="Press to decrease max number", command = maxValueDecrease)
generateNumberButton = Button(window, text="Press to generate number", command = randomNumberGenerate)
displayBox = Entry(window)

title.pack()
increaseButton.pack()
maxValueBox.pack()
decreaseButton.pack()
generateNumberButton.pack()
displayBox.pack()

window.mainloop()