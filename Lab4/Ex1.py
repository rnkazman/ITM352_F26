first = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last = input("Enter your last name: ")

full_name = first + " " + middle_initial + ". " + last
print("Your full name is:", full_name)

print(f"Your full name using F-strings is: {first} {middle_initial}. {last}")
print("Your full name using percent formatting is: %s %s. %s" % (first, middle_initial, last))
print("Your full name using format method is: {} {}. {}".format(first, middle_initial, last))
print("Your full name using list joins is: " + " ".join([first, middle_initial + ".", last]))
