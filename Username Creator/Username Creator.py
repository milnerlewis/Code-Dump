# # # # # Start Of Program ~-~


# Importing time module ~-~

import time

# # End of Importing time module ~-~


# Initial text ~-~

print("Welcome to the Username Creator!\n")

time.sleep(1)

# # End of Initial text ~-~


# Data gathering ~-~

fname = input("What is your first name? ")

print("\n")

time.sleep(0.5)

sname = input("What is your surname? ")

print("\n")

time.sleep(0.5)

age = input("How old are you? ")

print("\n")

time.sleep(0.5)

print("Creating username...\n\n")

time.sleep(2)

print ("Please wait...\n\n\n")

time.sleep(2)

# # # End of Data gathering ~-~


# Username creation section ~-~


# Changing the data types ~-~

fname = str(fname)

sname = str(sname)

age = int(age)

# # End of Changing the data types ~-~


# Making the names lowercase ~-~

fname = fname.lower()

sname = sname.lower()

# # End of lowercase names ~-~


# Changing age to make username more secure ~-~

age = age + 3

# # End of Changing age to make username more secure ~-~


# Username generation section ~-~

username = (f"{age}{sname}{fname[0]}")

# # End of Username generation section ~-~


# # # End of Username creation section ~-~


# Giving the user their Username ~-~

print("Your username is: \n")

print(f"{username}\n\n\n\n\n")

print("Thank you for using the Username Creator!\n\n\n")

# # # # # End Of Program ~-~