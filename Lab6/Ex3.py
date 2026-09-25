# Determine movie price. The rules are:
# - The normal price is $14
# - If someone is 65 or older, they pay $8.
# - If it is Tuesday, the price is $10.
# - If it is a matinee, the price is $5 for seniors and $8 otherwise
# Name: Rick Kazman
# Date: Sept. 25, 2026

age = 82
day = "Tuesday"
matinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8


print(f"Day: {day}, Matinee: {matinee}")
if (age >= 65):
    print("Welcome, senior")
else:
    print("Welcome, non-senior")

print(f"Ticket price is ${price:.2f}")
