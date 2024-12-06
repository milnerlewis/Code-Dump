import random

import time

lives = 10

play_again = "y"

random_number = (random.randint(1,100))

while "y" in play_again:

    user_guess = int(input("\n\n\nWhat number do you want to guess, 1-100? "))

    print(int(random_number)) # REMOVE AFTER TESTS

    if int(user_guess) == random_number:

        print("\nYou guessed the correct number, good job!\n\nYou have officially won!\n")

        play_again = input("\nWould you like to play again (y/n): ")

        play_again = play_again.lower()

        if "y" in play_again:

            random_number = (random.randint(1,100))

            lives = 10

        continue

    else:

        lives += -1


        if int(user_guess) > random_number:

            print("\nThe number is lower than your guess...\n")

        else:

            print("\nThe number is higher than your guess...\n")

        if lives > 0:

            print(f"\nYou are incorrect and lost a life!\n\nYou only have {lives} lives remaining!\n")

    if lives == 0:

        print("\nYou have ran out of lives.\n")

        play_again = input("\nWould you like to play again (y/n): ")

        play_again = play_again.lower()

    if "y" in play_again and lives == 0:

        random_number = (random.randint(1,100))

        lives = 10

if "n" in play_again:

    print("\n\nThank you for playing the number guess game!\n\n")