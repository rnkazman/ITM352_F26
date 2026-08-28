"""
Simple Calculator Program
Performs basic math operations: add, subtract, multiply, divide
Includes error handling for division by zero
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    """Main function to run the calculator"""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    
    try:
        # Get input from user
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
        
        # Display operation options
        print("\nChoose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            return
        
        # Display result
        print("\n" + "=" * 40)
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("=" * 40)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
