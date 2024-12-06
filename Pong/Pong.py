from tkinter import *
import time
import random
import winsound

tk = Tk()

gameCanvas = Canvas(tk, bg="black", height=250, width=750)
gameCanvas.pack()

xPosition1 = random.randint(75,675)
yPosition1 = random.randint(75,175)
xVelocity1 = random.randint(1,5)
yVelocity1 = random.randint(2,5)

xPosition2 = random.randint(75,675)
yPosition2 = random.randint(75,175)
xVelocity2 = random.randint(1,5)
yVelocity2 = random.randint(2,5)

i = 0

tempVal = 0

lastTime = time.time()

while True:

    i += 1

    xPosition1 = xPosition1 + xVelocity1
    yPosition1 = yPosition1 + yVelocity1

    if xPosition1 > 725 or xPosition1 < 0:
        xVelocity1 = xVelocity1 * -1
        winsound.Beep(200,1)

    if yPosition1 > 210 or yPosition1 < 0:
        yVelocity1 = yVelocity1 * -1
        winsound.Beep(200,1)

    xPosition2 = xPosition2 + xVelocity2
    yPosition2 = yPosition2 + yVelocity2

    if xPosition2 > 725 or xPosition2 < 0:
        xVelocity2 = xVelocity2 * -1
        winsound.Beep(200,1)

    if yPosition2 > 210 or yPosition2 < 0:
        yVelocity2 = yVelocity2 * -1
        winsound.Beep(200,1)


    gameCanvas.delete("all")

    if i > 0 and i <= 100:

        oval1 = gameCanvas.create_oval(xPosition1, yPosition1, xPosition1 + 40, yPosition1 + 40, fill="limegreen")
        oval2 = gameCanvas.create_oval(xPosition2, yPosition2, xPosition2 + 40, yPosition2 + 40, fill="darkred")
        
    if i > 100 and i <= 200:

        oval1 = gameCanvas.create_oval(xPosition1, yPosition1, xPosition1 + 40, yPosition1 + 40, fill="cyan")
        oval2 = gameCanvas.create_oval(xPosition2, yPosition2, xPosition2 + 40, yPosition2 + 40, fill="yellow")

    if i > 200 and i <= 300:

        oval1 = gameCanvas.create_oval(xPosition1, yPosition1, xPosition1 + 40, yPosition1 + 40, fill="purple")
        oval2 = gameCanvas.create_oval(xPosition2, yPosition2, xPosition2 + 40, yPosition2 + 40, fill="limegreen")

    if i > 300 and i <= 400:
        
        oval1 = gameCanvas.create_oval(xPosition1, yPosition1, xPosition1 + 40, yPosition1 + 40, fill="darkred")
        oval2 = gameCanvas.create_oval(xPosition2, yPosition2, xPosition2 + 40, yPosition2 + 40, fill="cyan")

    if i > 400 and i <= 500:

        oval1 = gameCanvas.create_oval(xPosition1, yPosition1, xPosition1 + 40, yPosition1 + 40, fill="yellow")
        oval2 = gameCanvas.create_oval(xPosition2, yPosition2, xPosition2 + 40, yPosition2 + 40, fill="purple")

        if i >= 500:

            i = 0

    if ((xPosition2 - 35 <= xPosition1 or xPosition1 > xPosition2 + 35) and
        (yPosition1 - 35 <= yPosition2 or yPosition2 > yPosition1 + 35) and
        (yPosition2 - 35 <= yPosition1 or yPosition1 > yPosition2 + 35) and
        (xPosition1 - 35 <= xPosition2 or xPosition2 > xPosition1 + 35)):

        if xPosition1 < xPosition2 and (time.time() - 0.2 > lastTime):

            xVelocity2 = -xVelocity2

            if xPosition1 > 0:
                xPosition1 -= 35

            else:
                xPosition1 += 35

            lastTime = time.time()

            tempVal += 1

            print(tempVal)

            winsound.Beep(200,1)

        elif xPosition2 < xPosition1 and (time.time() - 0.2 > lastTime):

            xVelocity1 = -xVelocity1

            if xPosition2 > 0:
                xPosition2 -= 35

            else:
                xPosition2 += 35

            lastTime = time.time()

            tempVal += 1

            print(tempVal)

            winsound.Beep(200,1)
        
        if yPosition1 < yPosition2 and (time.time() - 0.2 > lastTime):

            yVelocity2 = -yVelocity2

            if yPosition1 > 0:
                yPosition1 -= 35

            else:
                yPosition1 += 35

            # yPosition1 += 40

            lastTime = time.time()

            tempVal += 1

            print(tempVal)

            winsound.Beep(200,1)

        elif yPosition2 < yPosition1 and (time.time() - 0.2 > lastTime):

            yVelocity1 = -yVelocity1

            if yPosition2 > 0:
                yPosition2 -= 35

            else:
                yPosition2 += 35

            lastTime = time.time()

            tempVal += 1

            print(tempVal)

            winsound.Beep(200,1)


    tk.update()
    time.sleep(0.01)


tk.mainloop()