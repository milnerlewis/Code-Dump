# # # # # Start of program ~-~


# Set up marking values ~-~

incorrect = int(0)

at_symbol = True

at_location = -1

spaces = False

dot = False

dot_location = -1

# # # End of marking values setup ~-~


# Initial data gathering ~-~

print("Welcome to the Email Checker!\n")

user_email = input("What is your email address? ")

# #  End of Initial data gathering ~-~


# Email checks ~-~

for i in range(0 , len(user_email)):

    print(user_email[i])

# If statement ~-~

    if user_email[i] == "@":

        at_location = i

# # End of If statement ~-~


# If statement ~-~

    if user_email[i] == ".":
        dot_location = i

# # End of If statement ~-~


# If statement ~-~

    if "@" not in user_email:

        at_symbol = False

        print("@ == False")

    else:

        print("@ == True")

# # End of If statement ~-~


# If statement ~-~

    
    if " " in user_email:

        spaces = True

        print("Whitespace == True")

    else:

        print("Whitespace == False")

# # End of If statement ~-~


# If statement ~-~

    if "." in user_email:

        dot = True

        print("Dot == True\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    else:

        print("Dot == False\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

# # End of If statement ~-~


# # # End of email checks ~-~


# If statement ~-~

if dot == False:

    incorrect += 1

# # End of If statement ~-~


# If statement ~-~

if spaces == True:

    incorrect += 1

# # End of If statement ~-~


# If statement ~-~

if at_symbol == False:

    incorrect += 1

# # End of If statement ~-~



# Check results ~-~

if at_location >= 1 and dot_location > at_location + 1 and dot_location < len(user_email) - 2:

    if incorrect > 0:

        print(f"\n\n\nUnfortunately, your email ({user_email}) has failed {incorrect} of the 3 tests.\n")

        print(f"\nHere is the results of the test:\nContains @: {at_symbol}     (needs to be true to pass)\nContains spaces: {spaces}     (needs to be false to pass)\nContains a dot: {dot}     (needs to be true to pass)\n")

    else:

        print(f"\n\nYour email ({user_email}) has passed the email check test!\n")

else:
    
    print("\n\n\nYour email format is invalid, please try again.")

# # End of Check results ~-~


# Final statement ~-~

print("\n\nThank you for using the Email Checker!\n\n")

# # End of Final statement ~-~


# # # # # End of program ~-~