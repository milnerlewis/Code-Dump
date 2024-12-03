import random

lives = 5

play_again = "y"

number = random.randint(1,100)

print("\nWelcome to Higher or Lower!\n\n")

while "y" in play_again:

    guess = input("\nWhat number would you like to guess?")

    if guess.isdigit() == True:

        guess = int(guess)

    else:

        print("\nInvalid guess (Guess not = digit), please try again.")

        continue

    if guess == number:

        print("\nYou guessed the correct number, congratulations!")

        play_again = input("\nWould you like to play again (y/n)? ")

        play_again = play_again.lower()

        if "y" in play_again:

            number = random.randint(1,100)

        continue
    
    if guess > number:
        
        lives += -1

        print(f"\nThe number is lower than your guess. You have {lives} lives remaining.")

    if guess < number:

        lives += -1

        print(f"\nThe number is higher than your guess.\nYou have {lives} lives remaining.")

    if lives <= 0:

        print(f"\nYou have ran out of lives.\n\nThe number was {number}\n\n")

        play_again = input("\nWould you like to play again (y/n)? ")

        play_again = play_again.lower()

        if "y" in play_again:

            number = random.randint(1,100)

        continue



if "n" in play_again:

    print("\n\n\n\n\nThank you for playing Higher or Lower!\n\n\n\n\n")
    