import random

playAgain = "y"
shots = 25
rowGuess = ""
columnGuess = ""
numOfShip = 10
gameWin = False
misses = 0
shipGuesses = [[[0][0]]]


def hitProc(boardValues, rowGuess, columnGuess):
    if (rowGuess - 1) < 0 or (rowGuess > 3):
        print("Row value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues
    elif (columnGuess - 1) < 0 or (columnGuess > 3):
        print("Column value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues
    boardValues[int(rowGuess) - 1][int(columnGuess) - 1] = "H"
    print("hitProc",rowGuess, columnGuess, boardValues)
    return boardValues

assert hitProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 2, 1) == [['O', 'O', 'O'], ['H', 'O', 'O'], ['O', 'O', 'O']]
assert hitProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 0, 1) == [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
assert hitProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 2, 7) == [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]


def missProc(boardValues, rowGuess, columnGuess, shots):
    if (rowGuess - 1) < 0 or (rowGuess > 3):
        print("Row value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues, shots
    elif (columnGuess - 1) < 0 or (columnGuess > 3):
        print("Column value was not accepted")
        columnGuess = ""
        rowGuess = ""
        return boardValues, shots
    boardValues[rowGuess - 1][columnGuess - 1] = "X"
    shots -= 1
    print("missProc",rowGuess, columnGuess, boardValues, shots)
    return boardValues, shots

#boardValuesNew, shotsNew =  missProc(boardValues, rowGuess, columnGuess, shots)

assert missProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 2, 1, 10) == ( [['O', 'O', 'O'], ['X', 'O', 'O'], ['O', 'O', 'O']], 9)
assert missProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 0, 1, 10) == ([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 10)

assert missProc([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 2, 7, 10) == ([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']], 10)



def guessProc(rowGuess, columnGuess, shipGuesses, gridSize):
    rowGuess = input(f"What row would you like to select (1-{gridSize})? ")
    columnGuess = input(f"What column would you like to select (1-{gridSize})? ")
    if (rowGuess.isdigit() == True) or (columnGuess.isdigit() == True):
        shipGuesses.insert(0,[rowGuess, columnGuess])


exit()

'''
print(f"\n\nWelcome to battleships!")
gridSize = int(input("What would you like the grid size to be (input)x(input)? "))
print(f"\n\nThe game is simple, destroy the ships in the 10x10 grid without running out of lives.\n\nYou will have {shots} and you will gain a replacement life for every hit you get.\n\nWhen selecting your point to shoot at, you will need to follow the method of 'Along the corridor and up the stairs'.\nThis will mean giving your x/row number first, followed by the y/column number afterwards.\n\nGood luck!")


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
        rowNum += 11
        output += str(rowNum).center(3, " ")
        for value in boardRow:
            output += value.center(3, " ")
        output += "\n"
    return output

def missProc():
    boardValues[rowGuess][columnGuess] = "X"
    shots -= 1

def guessProc():
    global rowGuess
    global columnGuess
    global shipGuesses
    rowGuess = int(input(f"What row would you like to select (1-{gridSize})? "))
    columnGuess = int(input(f"What column would you like to select (1-{gridSize})? "))
    shipGuesses.insert(0,[rowGuess, columnGuess])


def shipGenerate():
    global ships
    ships = ([[random.randint(1,(gridSize - 1)),random.randint(1,(gridSize - 1))] for a in range(numOfShip)])

while "y" in playAgain:
    
    shipGenerate()
    

    while shots > 0 or gameWin == False:
        print(boardToStr(boardValues))
        print(guessProc())
        
        if ((str(rowGuess)).isdigit() == False) or ((str(columnGuess)).isdigit() == False) or (rowGuess > gridSize) or (columnGuess > gridSize):
            print(f"The co-ordinates that you entered are invalid.")


        elif shipGuesses in ships:

            #[rowGuess , columnGuess] == ships[0:shipNum]:
            
            hitProc()
            print(f"Good job, you have sunk a ship. You have not lost any ammunition, meaning you are still on {shots} shots remaining.\nYou have {numOfShip} ships remaining.")
                
        else:
            missProc()
            print(f"You missed. You have been left with {shots} shots remaining.")


        
            
            '''