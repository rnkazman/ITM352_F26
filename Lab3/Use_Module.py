import HandyMath

# Get two numbers from the user for the HandyMath calculations.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Display results calculated by functions from the HandyMath module.
print(f"The midpoint of {number1} and {number2} is {HandyMath.midpoint(number1, number2)}.")
print(f"The square root of {number1} squared is {HandyMath.squareroot(number1 ** 2)}.")
print(f"{number1} raised to the power of {number2} is {HandyMath.exponent(number1, number2)}.")
print(f"The maximum of {number1} and {number2} is {HandyMath.max(number1, number2)}.")
print(f"The minimum of {number1} and {number2} is {HandyMath.min(number1, number2)}.")
