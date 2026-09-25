# Testing the use of assertions.

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    assert celsius >= -273.15, "Temperature cannot be below absolute zero."
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


print(celsius_to_fahrenheit(0))    # Should print 32.0
print(celsius_to_fahrenheit(100))  # Should print 212.0
print(celsius_to_fahrenheit(-300))  # Should raise an AssertionError
