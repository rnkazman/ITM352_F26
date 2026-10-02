# Try – Except example
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: You can't divide by zero.")
    else:
        print("Division succeeded!")
    finally:
        print("Done attempting the division.\n")

divide_numbers()
