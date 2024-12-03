import math

"""
shed_side_one_area = round((shed_side_length_one * 1000) * (shed_side_height_one * 1000))

brick_area_number_one = (float(shed_side_one_area) / float(brick_area)) * 2

shed_side_two_area = int(shed_side_length_two * 1000) * int(shed_side_height_two * 1000)

brick_number_area_two = round((int(shed_side_two_area) / int(brick_area)) * 2)

overall_brick_cost = ((int(brick_area_number_one) + int(brick_number_area_two)) * int(brick_value_per)) / 100

print(f"\n\nThe cost of your Brick shed would be approximately £{round(overall_brick_cost)}.")
"""

side1a = "5" # Meters

side2a = "3" # Meters

side1b = "2" # Meters

side2b = "2" # Meters

brick_area = "1687" # CM

brick_value_per = "82" # Pense not £

# brick_num1 = (((int(side1a * 100) * int(side2a * 100))) / int(brick_area)) * 2

brick_num1_step1 = int(side1a) * 100

brick_num1_step2 = int(side1b) * 100

brick_num1_step3 = (brick_num1_step1 * brick_num1_step2) * 2

brick_num1 = brick_num1_step3 / (int(brick_area))

brick_num2_step1 = int(side2a) * 100

brick_num2_step2 = int(side2b) * 100

brick_num2_step3 = (brick_num2_step1 * brick_num2_step2) * 2

brick_num2 = brick_num2_step3 / (int(brick_area))

brick_cost = ((int(brick_num1) + int(brick_num2)) * int(brick_value_per)) / 100

print(brick_num1)

print(f"You will need {round(brick_num1 + brick_num2)} bricks.\nThis will cost £{brick_cost}.")