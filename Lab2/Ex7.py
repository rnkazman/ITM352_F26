# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Name: Rick Kazman
# Date: Sept. 4, 2026

fahrenheit_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)

celsius_value = (fahrenheit_float - 32) * 5 / 9

celsius_value = round(celsius_value, 2)

print("You entered:", fahrenheit_float)
print("The temperature in Celsius is:", celsius_value)
