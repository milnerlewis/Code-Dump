# Importing modules ~-~

import math

# # # End of Importing modules ~-~


# Opening statement ~-~

print("\n\nWelcome to the Shed Calculator!")

# # # End of Opening statement ~-~


# Storing initial variables ~-~


# Global variables setup ~-~

side1a = ""

side2a = ""

side1b = ""

side2b = ""

building_material = ""

# # End of Global variables setup ~-~

brick_value_per = "82" # IN PENSE NOT POUNDS

brick_area = "1687" # IN MM NOT M

block_value_per = "245" # IN PENSE NOT POUNDS

block_area = "9460" # IN MM NOT M

side1a = input("\nWhat will be one wall length of your shed (in meters)? ")

if side1a.isdigit() == True:

    side1b = input("\nWhat is the height of this wall (in meters)? ")

    if side1b.isdigit() == True:

        side2a = input("\nWhat will be the other wall length of your shed (in meters)? ")

        if side2a.isdigit() == True:

            side2b = input("\nWhat is the height of this wall (in meters)? ")

            if side2b.isdigit() == True:

                building_material = input("\nWill you be using Bricks or Blocks? ")

            else:

                print("\n\nThe side height you just input was invalid, please make sure there are no decimal places or white space and try again.")

        else:

            print("\n\nThe side length you just input was invalid, please make sure there are no decimal places or white space and try again.")

    else:

        print("\n\nThe side height you just input was invalid, please make sure there are no decimal places or white space and try again.")

else:
    print("\n\nThe side length you just input was invalid, please make sure there are no decimal places or white space and try again.")

# # # End of Storing initial variables ~-~


# Data manipulation ~-~

building_material = building_material.lower()

# # End of Data manipulation ~-~


"""
shed_side_one_area = round((side1a * 1000) * (side2a * 1000))

brick_area_number_one = (float(shed_side_one_area) / float(brick_area)) * 2

shed_side_two_area = int(side1b * 1000) * int(side2b * 1000)

brick_number_area_two = round((int(shed_side_two_area) / int(brick_area)) * 2)

overall_brick_cost = ((int(brick_area_number_one) + int(brick_number_area_two)) * int(brick_value_per)) / 100

print(f"\n\nThe cost of your Brick shed would be approximately £{round(overall_brick_cost)}.")
"""


# Brick section ~-~

if "bri" in building_material or "brick" in building_material:

    brick_num1_step1 = int(side1a) * 100

    brick_num1_step2 = int(side1b) * 100

    brick_num1_step3 = (brick_num1_step1 * brick_num1_step2) * 2

    brick_num1 = brick_num1_step3 / (int(brick_area))

    brick_num2_step1 = int(side2a) * 100

    brick_num2_step2 = int(side2b) * 100

    brick_num2_step3 = (brick_num2_step1 * brick_num2_step2) * 2

    brick_num2 = brick_num2_step3 / (int(brick_area))

    brick_cost = ((int(brick_num1) + int(brick_num2)) * int(brick_value_per)) / 100

    print(f"You will need {round(brick_num1 + brick_num2)} bricks.\nThis will cost £{brick_cost}.")

# # # End of Brick shed ~-~


# Block section ~-~

elif "blo" in building_material or "block" in building_material:

    block_num1_step1 = int(side1a) * 100

    block_num1_step2 = int(side1b) * 100

    block_num1_step3 = (block_num1_step1 * block_num1_step2) * 2

    block_num1 = block_num1_step3 / (int(block_area))

    block_num2_step1 = int(side2a) * 100

    block_num2_step2 = int(side2b) * 100

    block_num2_step3 = (block_num2_step1 * block_num2_step2) * 2

    block_num2 = block_num2_step3 / (int(block_area))

    block_cost = ((int(block_num1) + int(block_num2)) * int(block_value_per)) / 100

    print(f"You will need {round(block_num1 + block_num2)} blocks.\nThis will cost £{block_cost}.")

# # # End of Block section ~-~


# Invalid building material ~-~

else:
    print('\n\nThe building material entered was invalid, please try again with either "Brick" or "Block".\n\n')

# # # # # End of program ~-~