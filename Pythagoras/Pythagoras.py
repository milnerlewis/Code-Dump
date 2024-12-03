"""
a^2 + b^2 = c^2
"""


# Importing modules

import math

# # End of Importing modules


# Welcome message ~-~

print("Welcome to the Pythagoras Calculator!\n\n\n")

# # End of Welcome message ~-~


# Beginning data collection ~-~


# Player 1 co-ordinates ~-~

point_a_x = input("What is the x co-ordinate of the first player (Player A)? ")

point_a_y = input("\nWhat is the y co-ordinate of the first player (Player A)? ")

# Player 2 co-ordinates ~-~

point_b_x = input("\nWhat is the x co-ordinate of the second player (Player B)? ")

point_b_y = input("\nWhat is the y co-ordinate of the second player (Player B)? ")

# # # End of data collection ~-~


# Data manipulation

point_a_x = point_a_x.strip()

point_a_y = point_a_y.strip()

point_b_x = point_b_x.strip()

point_b_y = point_b_y.strip()

# # End of Data manipulation


# Conditional calculation ~-~


# Pre-Calculation validation ~-~

if point_a_x.isdigit() == True:
    
    if point_a_y.isdigit() == True:
        
        if point_b_x.isdigit() == True:
            
            if point_b_y.isdigit() == True:

# # End of Pre-Calculation validation ~-~


# Pre calculation conversions ~-~

                point_a_x = float(point_a_x)

                point_a_y = float(point_a_y)

                point_b_x = float(point_b_x)

                point_b_y = float(point_b_y)

# # End of Pre calculation conversions ~-~

# Beginning of calculation ~-~

                a = point_a_x - point_b_x

                b = point_a_y - point_b_y

                c_square = (a*a)+(b*b)

                c = math.sqrt(c_square)

# # End of calculation ~-~


# Final value reveal ~-~

                print(f"\n\nThe players are {c} away from each other.")

                print("\n\nThank you for using the Pythagoras Calculator!\n\n")

# # End of Final value reveal ~-~


# # # End of Conditional calculation ~-~


# Incorrect value/s statements ~-~


# Statement one ~-~

            else:

                print("\n\nYour y co-ordinate for Player B was invalid, please try again.\n\n")

# # End of Statement one ~-~


# Statement two ~-~

        else:
            print("\n\nYour x co-ordinate for Player B was invalid, please try again.\n\n")

# # End of Statement two ~-~


# Statement three ~-~

    else:
        print("\n\nYour y co-ordinate for Player A was invalid, please try again.\n\n")

# # End of Statement three ~-~


# Statement four ~-~

else:
    print("\n\nYour x co-ordinate for Player A was invalid, please try again.\n\n")

# # End of Statement four ~-~


# # # End of Incorrect value/s statements ~-~


# # # # # End of program ~-~