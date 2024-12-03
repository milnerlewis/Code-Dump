import random

playAgain = "y"
shots = 25
rowGuess = ""
columnGuess = ""
numOfShip = 10
gameWin = False
misses = 0
shipGuesses = [[[0][0]]]
numOfShipRemaining = 10



print(f"\n\nWelcome to battleships!")
print(f"\n\nThe game is simple, destroy the ships in the 10x10 grid without running out of lives.\n\nYou will have {shots} and you will gain a replacement life for every hit you get.\n\nWhen selecting your point to shoot at, you will need to follow the method of 'Along the corridor and up the stairs'.\nThis will mean giving your x/row number first, followed by the y/column number afterwards.\n\nGood luck!")
gridSize = int(input("What would you like the grid size to be (input)x(input)? "))


boardValues = ([["O"] * gridSize for a in range(gridSize)])
boardColumns = ["*","1","2","3","4","5","6","7","8","9","10"]

def boardToStr(boardValues):
    output = " * "
    boardHeading = 0
    for i in range(gridSize):
        boardHeading =  str(i+1)
        output += boardHeading.center(3, " ")
    output += "\n"
    rowNum = 0
    for boardRow in boardValues:
        rowNum += 1
        output += str(rowNum).center(3, " ")
        for value in boardRow:
            output += value.center(3, " ")
        output += "\n"
    return output

def missProc(boardValues, rowGuess, columnGuess, shots):
    rowGuess = int(rowGuess)
    rowGuess -= 1
    columnGuess = int(columnGuess)
    columnGuess -= 1
    if (rowGuess) < 0 or (rowGuess > gridSize):
        print("Row value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return shots
    elif columnGuess  < 0 or (columnGuess > gridSize):
        print("Column value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return shots
    else:
        boardValues[rowGuess][columnGuess] = "X"
        shots -= 1
        return shots

def hitProc(boardValues, rowGuess, columnGuess):
    rowGuess = int(rowGuess)
    columnGuess = int(columnGuess)
    if rowGuess < 0 or (rowGuess > gridSize):
        print("Row value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues
    elif columnGuess < 0 or (columnGuess > gridSize):
        print("Column value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues
    boardValues[rowGuess][columnGuess] = "H"
    numOfShipRemaining -= 1
    return boardValues

def guessProc(rowGuess, columnGuess, shipGuesses, gridSize):
    rowGuess = input(f"What row would you like to select (1-{gridSize})? ")
    print(rowGuess)
    columnGuess = input(f"What column would you like to select (1-{gridSize})? ")
    print(columnGuess)
    return shipGuesses


def shipGenerate():
    global ships
    ships = ([[random.randint(1,(gridSize - 1)),random.randint(1,(gridSize - 1))] for a in range(numOfShip)])

while "y" in playAgain:
    
    shipGenerate()
    

    while shots > 0 or gameWin == False or numOfShipRemaining != 0:
        print(boardToStr(boardValues))
        rowGuess = input(f"What row would you like to select (1-{gridSize})? ")
        columnGuess = input(f"What column would you like to select (1-{gridSize})? ")
        
        if [rowGuess , columnGuess] in ships:
            
            hitProc(boardValues, rowGuess, columnGuess)
            print(f"Good job, you have sunk a ship. You have not lost any ammunition, meaning you are still on {shots} shots remaining.\nYou have {numOfShip} ships remaining.")
                
        else:
            missProc(boardValues, rowGuess, columnGuess, shots)
            print(f"You missed. You have been left with {shots} shots remaining.")

        if numOfShipRemaining == 0:
            print("Congratulations, you have sunk all of the ships!")
            continue

        elif shots == 0:
            print("You have ran out of shots and failed to sink all of the ships...")
            continue

    playAgain = ((input("Would you like to start another game (y/n)? ")).lower())
        
            
