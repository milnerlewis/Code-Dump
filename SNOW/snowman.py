from tkinter import *
import time

tk = Tk()

myLabel = Label(tk, text = "Merry Christmas")
myLabel.pack()

C = Canvas(tk, bg="black", height=500, width=500)
C.pack()

while 1:
    C.delete("all")
    topOval = C.create_oval(200, 50, 300, 155, fill="white")
    eyeLeft = C.create_oval(220, 85, 235, 100, fill="black")
    eyeRight = C.create_oval(265, 85, 280, 100, fill="black")
    nose = C.create_oval(247, 100, 253, 125, fill="orange")
    
    middleOval = C.create_oval(175, 150, 325, 305, fill="white")
    buttonBottom = C.create_oval(240, 260, 260, 280, fill="black")
    buttonMiddle = C.create_oval(240, 220, 260, 240, fill="black")
    buttonTop = C.create_oval(240, 180, 260, 200, fill="black")
    
    bottomOval = C.create_oval(150, 300, 350, 505, fill="white")
    tk.update()
    time.sleep(0.01)
