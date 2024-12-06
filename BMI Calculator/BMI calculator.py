# Initial statement ~-~

print("Welcome to the BMI Calculator.\n")

# # End of Initial statement ~-~


# Data collection ~-~

measuring_unit = input("Will your values be in metric(met) or imperial(imp) units? ")

# # End of Data collection ~-~


# Data manipulation ~-~

measuring_unit = measuring_unit.lower()

# # End of Data manipulation ~-~


# Imperial units section ~-~

if "imp" in measuring_unit:

    user_height = input("\nWhat is your height in inches (To the nearest integer)? ")

    user_weight = input("\nWhat is your weight in pounds (To the nearest integer)? ")

    if user_height.isdigit() == True:

        if user_weight.isdigit() == True:

            user_height = float(user_height)

            user_weight = float(user_weight)

# Imperial calculation ~-~

            bmi_calc_1 = float(user_height) * float(user_height)

            bmi_calc_2 = float(user_weight) / float(bmi_calc_1)

            user_bmi_imp = float(bmi_calc_2) * 703

# # End of Imperial calculation ~-~



# BMI classification check ~-~

            if user_bmi_imp < 15.0:
    
                bmi_classification = "Very severely underweight"
    
            if user_bmi_imp >= 15.0 and user_bmi_imp < 15.6:

                bmi_classification = "Severely underweight"

            if user_bmi_imp >= 16 and user_bmi_imp < 18.5:

                bmi_classification = "Underweight"

            if user_bmi_imp >= 18.5 and user_bmi_imp < 25:
        
                bmi_classification = "Normal/Healthy"

            if user_bmi_imp >= 25 and user_bmi_imp < 30:

                bmi_classification = "Overweight"

            if user_bmi_imp >= 30 and user_bmi_imp < 35:

                bmi_classification = "Moderately obese"

            if user_bmi_imp >= 35 and user_bmi_imp < 40:

                bmi_classification = "Severely obese"

            if user_bmi_imp >= 40:
            
                bmi_classification = "Very severely obese"

# # End of BMI classification check ~-~


# BMI reveal ~-~

            print(f"\nYour BMI is {user_bmi_imp}.\nThis classifies you as {bmi_classification}.\n")

# # End of BMI reveal ~-~


# Invalid values statements ~-~

        else:

         print("The entered weight is invalid, please try again.")

    else:

        print("The entered height is invalid, please try again.")

# # End of Invalid values statement ~-~


# Final statement ~-~

        print("\nThank you for using the BMI Calculator!\n\n")

# # End of Final statement ~-~


# # # End of Imperial units section ~-~


# Metric units section ~-~

elif "met" in measuring_unit:

    user_height = str(input("\nWhat is your height in centimeters (To the nearest integer)? "))

    user_weight = str(input("\nWhat is your weight in kilograms (To the nearest integer)? "))

    if user_height.isdigit() == True:

        if user_weight.isdigit() == True:

            user_height = float(user_height)

            user_weight = float(user_weight)

# Imperial calculation ~-~

            user_height = float(user_height / 100)

            user_bmi_met = (float(user_weight) / (float(user_height) * float(user_height)))

# # End of Imperial calculation ~-~


# BMI classification check ~-~

            if user_bmi_met < 15.0:
    
                bmi_classification = "Very severely underweight"
    
            if user_bmi_met >= 15.0 and user_bmi_met < 15.6:

                bmi_classification = "Severely underweight"

            if user_bmi_met >= 16 and user_bmi_met < 18.5:

                bmi_classification = "Underweight"

            if user_bmi_met >= 18.5 and user_bmi_met < 25:
        
                bmi_classification = "Normal/Healthy"

            if user_bmi_met >= 25 and user_bmi_met < 30:

                bmi_classification = "Overweight"

            if user_bmi_met >= 30 and user_bmi_met < 35:

                bmi_classification = "Moderately obese"

            if user_bmi_met >= 35 and user_bmi_met < 40:

                bmi_classification = "Severely obese"

            if user_bmi_met >= 40:

                bmi_classification = "Very severely obese"

# # End of BMI classification check ~-~


# Invalid values statements ~-~

        else:

            print("The entered weight is invalid, please try again.")

    else:

        print("The entered height is invalid, please try again.")

# # End of Invalid values statement ~-~


# BMI reveal ~-~

    print(f"\nYour BMI is {user_bmi_met}.\nThis classifies you as {bmi_classification}.\n")

# # End of BMI reveal ~-~


# Final statement ~-~

    print("\nThank you for using the BMI Calculator!\n\n")

# # End of Final statement ~-~


# # # End of Metric units section ~-~


# Initial else statement ~-~

else:
    print("\n!!!!!!!!!!\n!!!!!!!!!!\nThe chosen measuring unit was invalid, please try again.\n!!!!!!!!!!\n!!!!!!!!!!\n")

# # # End of Initial else statement ~-~

# # # # # End of program ~-~