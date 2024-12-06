import math

import random

addToTotal = "y"

continueLoop = "y"

totalCost = 0

print("Welcome to the Profit-Loss Calculator!\n")

while "y" in continueLoop:

    itemPrice = 0

    buyPrice = input("What was the initial cost of your item? ")

    sellPrice = input("How much are you selling this item for? ")

    addToTotal = str(input("Would you like to add the total profit/loss onto your running total (y/n)? "))

    if (buyPrice.isdigit() != True) or (sellPrice.isdigit() != True):
        print("The values given were not accepted, please try again.")

    else:
        buyPrice = int(buyPrice)
        sellPrice = int(sellPrice)
        if buyPrice < sellPrice:
            itemPrice = sellPrice - buyPrice
            if "y" in addToTotal:
                totalCost += itemPrice
            print(f"This item would cost you {itemPrice} to sell, meaning you would be making money on this item.\n")

        else:
            itemPrice = buyPrice - sellPrice
            if "y" in addToTotal:
                totalCost -= itemPrice
            print(f"This item would cost you {itemPrice} to sell, meaning you would be losing money on this item.\n")

    print(f"Your running total is {totalCost}.\n")

    continueLoop = input("Would you like to add another item (y/n)? ")

print("Thank you for using the Profit-Loss Calculator!")




