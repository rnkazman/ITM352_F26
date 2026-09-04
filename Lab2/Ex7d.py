# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Create the conversion as function.
# Name: Rick Kazman
# Date: Sept. 4, 2026

def F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    rounded_celsius = round(celsius, 2)
    return rounded_celsius


fahrenheit_input = input("Enter a temperature in Fahrenheit: ")
fahrenheit_float = float(fahrenheit_input)

celsius_value = F_to_C(fahrenheit_float)

print("You entered:", fahrenheit_float)
print("The temperature in Celsius is:", celsius_value)
