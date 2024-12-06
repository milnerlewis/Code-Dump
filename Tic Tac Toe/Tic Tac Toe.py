boardValues = ([["-"] * 3 for a in range(3)])

def boardToStr(boardValues):
    output = " * "
    boardHeading = 0
    for i in range(3):
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

def guessValidation(rowGuess, columnGuess):
    if ((rowGuess.isdigit() != True) or
        (columnGuess.isdigit() != True) or
        (int(rowGuess) > 3 or int(rowGuess) < 1) or
        (int(columnGuess) > 3 or int(columnGuess) < 1) or
        (boardValues[int(rowGuess) - 1][int(columnGuess) - 1] == "X") or
        (boardValues[int(rowGuess) - 1][int(columnGuess) - 1] == "O")):
            return False

    else:
        return True          

print("\n\n\n\n\n\n\n\n\n\nWelcome to Tic Tac Toe!!!\n\n\n")

gameContinue = "y"
gameOver = False

while "y" in gameContinue:

    gameOver = False
    boardValues = ([["-"] * 3 for a in range(3)])

    while False == gameOver:

        validGuess = "n"

        # # # # # Player One

        print(boardToStr(boardValues))

        while validGuess == "n":

            rowGuess = input("\nWhat row would you like to guess x(1-3)? ")

            columnGuess = input("\nWhat column would you like to guess x(1-3)? ")

            if guessValidation(rowGuess, columnGuess) == False:
                    
                print("\n\nThe guess was not valid.")
                validGuess = "n"

            else:
                rowGuess = int(rowGuess)
                columnGuess = int(columnGuess)

                validGuess = "y"

                boardValues[int(rowGuess) - 1][int(columnGuess) - 1] = "X"

        print(boardToStr(boardValues))

        # # # # # End of Player One
        print( "\nboardValues[0].count('X')", boardValues[0].count('X'))

        lRow1 = [boardValues[i][0] for i in range(3)]

        print("\nlRow1", lRow1)
        if ((boardValues[0][0] == "X" and boardValues[0][1] == "X" and boardValues[0][2] == "X") or
            (boardValues[1][0] == "X" and boardValues[1][1] == "X" and boardValues[1][2] == "X") or
            (boardValues[2][0] == "X" and boardValues[2][1] == "X" and boardValues[2][2] == "X") or
            (boardValues[0][0] == "X" and boardValues[1][0] == "X" and boardValues[2][0] == "X") or
            (boardValues[0][1] == "X" and boardValues[1][1] == "X" and boardValues[2][1] == "X") or
            (boardValues[0][2] == "X" and boardValues[1][2] == "X" and boardValues[2][2] == "X") or
            (boardValues[0][0] == "X" and boardValues[1][1] == "X" and boardValues[2][2] == "X") or
            (boardValues[0][2] == "X" and boardValues[1][1] == "X" and boardValues[2][0] == "X")):

                gameOver = True

                print("\n\nPlayer 1 has won!!")

                gameContinue = ((input("\n\n\nWould you like to play again (y/n)? ")).lower())

                continue
        
        validGuess = "n"

        while validGuess == "n":
        
            rowGuess = input("\nWhat row would you like to guess(1-3)? ")

            columnGuess = input("\nWhat column would you like to guess (1-3)? ")

            if guessValidation(rowGuess, columnGuess) == False:
                        
                print("\n\n\nThe guess was not valid.")
                validGuess = "n"

            else:
                rowGuess = int(rowGuess)
                columnGuess = int(columnGuess)

                validGuess = "y"
                boardValues[int(rowGuess) - 1][int(columnGuess) - 1] = "O"

        print(boardToStr(boardValues))

        if ((boardValues[0][0] == "O" and boardValues[0][1] == "O" and boardValues[0][2] == "O") or
            (boardValues[1][0] == "O" and boardValues[1][1] == "O" and boardValues[1][2] == "O") or
            (boardValues[2][0] == "O" and boardValues[2][1] == "O" and boardValues[2][2] == "O") or
            (boardValues[0][0] == "O" and boardValues[1][0] == "O" and boardValues[2][0] == "O") or
            (boardValues[0][1] == "O" and boardValues[1][1] == "O" and boardValues[2][1] == "O") or
            (boardValues[0][2] == "O" and boardValues[1][2] == "O" and boardValues[2][2] == "O") or
            (boardValues[0][0] == "O" and boardValues[1][1] == "O" and boardValues[2][2] == "O") or
            (boardValues[0][2] == "O" and boardValues[1][1] == "O" and boardValues[2][0] == "O")):

                gameOver = True

                print("\n\n\nPlayer 2 has won!!")

                gameContinue = input("\nWould you like to play again (y/n)? ")

                gameContinue = gameContinue.lower()

                continue
        
    if "n" in gameContinue:
                  
         continue
        

print("\n\n\nThank you for playing tic tac toe!\n\n\n")