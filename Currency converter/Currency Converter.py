#Initial inputs/data collection

print("Welcome to the Currency Converter. \nThese conversion are correct as of 05/09/2024")

gbp = int(input("How many GBP do you have (to the nearest whole number)? "))
user_currency = str(input("What currency would you like to convert your GBP into? \nPlease provide the abbreviation of the currency e.g., GBP, USD, EUR. "))

#Conversion equations
eur_convert = int(gbp * 1.19)
usd_convert = int(gbp * 1.32)
jpy_convert = int(gbp * 188.88)
aud_convert = int(gbp * 1.96)

#Final totals
if user_currency == "EUR":
    print("That will be: €" , eur_convert , "\nThank you for using the Currency Converter.")

elif user_currency == "USD":
    print("That will be: $" , usd_convert , "\nThank you for using the Currency Converter.")

elif user_currency == "JPY":
    print("That will be: ¥" , jpy_convert , "\nThank you for using the Currency Converter.")

elif user_currency == "AUD":
    print("That will be: $" , aud_convert , "\nThank you for using the Currency Converter.")

else : print("Your currency is not supported by the Converter, please try again with a compatible currency.")