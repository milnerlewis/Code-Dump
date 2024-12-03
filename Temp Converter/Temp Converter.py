# Initial data collection ~-~

temp = str(input("What do you have, Celsius or Fahrenheit? "))

# # End of Initial data collection ~-~


# Changing the string to lower case ~-~

temp = temp.lower()

# # End of Changing the string to lower case ~-~


# Conversion calculations ~-~

def cel_to_far():
    
    cel = float(input("Enter celsius: "))

    far = (cel * 1.8) + 32

    print("Fahrenheit is: " , far)

def far_to_cel():

    far = float(input("Enter Fahrenheit: "))
    
    cel = 5 / 9 * (far - 32)
    
    print("Celsius is: " , cel)

# Celsius --> Fahrenheit conversion ~-~

if temp == "cel":

    print(cel_to_far())

# # End of Celsius --> Fahrenheit conversion ~-~


# Fahrenheit --> Celsius conversion ~-~

elif temp == "far":

    print(far_to_cel())

# # End of Fahrenheit --> Celsius conversion ~-~


# End of Conversion calculations ~-~


# # # # # End Of Program ~-~