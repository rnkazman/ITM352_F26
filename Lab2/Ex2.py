# Ask the user to enter their birth year. Calculate their age based on the current year and print it out.
# Name: Rick Kazman
# Date: Sept. 2, 2026

birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year)

print("You entered:", birth_year)
print("Your age is: " + str(age))
