# This program prompts the user to enter a weight in pounds and then calculates and displays the equivalent weight in kilograms.
# Name: Rick Kazman
# Date: Sept. 4, 2026

#print("The weight in kilograms is:", float(input("Enter weight in pounds: "))*0.453592)

KG_TO_POUNDS = 0.453592
weight_in_pounds = input("Enter weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kilograms = weight_in_pounds_float * KG_TO_POUNDS

print("You entered:", weight_in_pounds_float)
print("The weight in kilograms is:", weight_in_kilograms)
