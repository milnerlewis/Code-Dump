# Setup start ~-~

shapelist = (("cube","triangle"))

shape = input("Do you have a Cube or Triangle? ")

shape = shape.lower()

# # Setup end ~-~


# Cuboid/Cube start ~-~

if shape == "cube":

# Input

    cubelength = float(input("Enter the length:")) # See below ~-~

# # End of Input ~-~


# Process ~-~

    cubevolume = cubelength * cubelength * cubelength # Volume calculation ~-~

    cubesurfacearea = ((cubelength * cubelength) * 6) # Surface Area calculation ~-~

# # End of Process ~-~


# Output ~-~

    print(f"The volume is: {cubevolume}") # Volume revealed ~-~

    print(f"The surface area is: {cubesurfacearea}") # Surface Area revealed ~-~

# # End of Output ~-~


# # # Cuboid/Cube end ~-~


# Triangle start ~-~


# Input ~-~

elif shape == "triangle":

    trianglelengtha = float(input("Enter the longest side length of your triangle: ")) # See below ~-~

    trianglelengthb = float(input("Enter a smaller side length of your triangle: ")) # Collecting values for the calculations ~-~

    trianglelengthc = float(input("Enter the final side length of your triangle: ")) # See above ~-~

# # End of Input ~-~


# Process ~-~

    trianglearea = ((trianglelengthb * trianglelengthc) / 2) # Area calculatoin ~-~

    triangleperimiter = (trianglelengtha + trianglelengthb + trianglelengthc) # Perimiter calculation ~-~

# # End of Process ~-~


# Output ~-~

    print(f"The area is: {trianglearea}")

    print(f"The perimiter is: {triangleperimiter}")

# End of Output ~-~


# # # Triangle end ~-~


# Final statement ~-~

print("\n\nThank you for using the shape calculator.\n\n")

# # End of Final statement ~-~


# # # # # End of program ~-~