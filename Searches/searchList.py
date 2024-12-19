import random as rand

simpleList = ["1","2","3","4","5"]
randNumList = []
running = "y"
firstFound = "."
secondFound = "."
thirdFound = "."
selectOperation = ""


def bubbleSort(numList):
    repeatSort = True
    
    while repeatSort == True:

        for j in range(len(numList)):
            for i in range(len(numList)-1):
                if numList[i] > numList[i + 1]:

                    tempVar = numList[i]
                    numList.pop[i]
                    numList.insert(i + 1, numList)

        return numList
        
def linearSearch(inputNum, numList):

    foundNum = False

    if inputNum.isdigit() == True and len(inputNum) > 0:
        inputNum = int(inputNum)

        for i in range(len(numList)):
            if numList[i] == inputNum:

                foundNum = True
                firstFound = "n"
                secondFound = "n"
                thirdFound = "n"

                if i == 0:
                    print(f"\nThe number {inputNum} has been found in the list.\nIt is the 1st number in the list.\n\n")
                    firstFound = "y"

                elif i == 1:
                    print(f"\nThe number {inputNum} has been found in the list.\nIt is the 2nd number in the list.\n\n")
                    secondFound = "y"

                elif i == 2:
                    print(f"\nThe number {inputNum} has been found in the list.\nIt is the 3rd number in the list.\n\n")
                    thirdFound = "y"

                elif i > 2:
                    print(f"\nThe number {inputNum} has been found in the list.\nIt is the {i+1}th number in the list.\n\n")

            if i == len(numList):
                pass

        if foundNum == False:
            print("\nYour number was not found in the list.")


    elif len(inputNum) > 1 or inputNum < 1:
        print("\nInvalid number selected, please ensure that your number is 1-9.")
        pass

    else:
        print("\nInvalid number selected.")
        pass

    return "\n!!Check complete!!"

def listGenerate(listLength, numStore):

    for i in range(int(listLength)):

        tempVar = rand.randint(1,10)
        numStore.append(tempVar)

    return numStore

while "y" in running:

    listLength = input("How long would you like your random list to be? ")

    if listLength.isdigit() == True:
        randNumList = listGenerate(listLength, randNumList)

    else:
        print("Invalid argument given, please try again.")
        pass

    selectOperation = input("**********************************************\n* Select the number of what you'd like to do *\n* 1. Bubble Sort                             *\n* 2. Linear Search                           *\n* 3. Insertion Sort                          *\n**********************************************\n\nInput: ")

    if selectOperation.isdigit():
        selectOperation = int(selectOperation)
    
    if selectOperation == 1:
        print(f"Before sort: {randNumList}\n")
        randNumList = bubbleSort(randNumList)
        print(f"After sort: {randNumList}")

    elif selectOperation == 2:
        numToFind = input("\nWhat number would you like to find (1-9)? ")

        foundNum = False

        linearSearch(numToFind, randNumList)

    running = input("\n\n\nWould you like to search for another number (y/n)? ")



print("\n\n\nThank you for your use, bye.")