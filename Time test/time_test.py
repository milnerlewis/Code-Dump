"""
distance: ~5 meters
start input
stop input
speed in m/s ---> speed in mph


1 m/s = 2.23693629 mph

5 m/s = 11.1846815
"""


# Importing modules ~-~

import time

# # End of Importing modules ~-~


# Introduction ~-~

print("Welcome to the Time Test.")

# # End of Introduction ~-~


# Initial data collection ~-~

distance = input("How far is the distance you will be traveling across in meters? ")

# # End of Initial data collection ~-~


# Timing ~-~

input("Press enter to start the timer.")

timer_start = time.time()

input("Press enter to end the timer.")

timer_end = time.time()

# # End of Timing ~-~


# Calculations ~-~

time_taken = timer_end - timer_start

meters_per_second = float(distance) / float(time_taken)

miles_per_hour = meters_per_second * 2.23693629

# # End of Calculations ~-~


# Final statement ~-~

print(f"Your speed in meters per second (m/s) is:\n{meters_per_second} m/s\n\n")

print(f"Your speed in miles per hour (mph) is:\n{miles_per_hour} mph\n\n")

print("Thank you for using the Time Test.")

# # End of Final statement ~-~

# # # # # End of program ~-~