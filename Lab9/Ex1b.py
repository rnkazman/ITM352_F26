# Open a file using "with"

with open("names.txt", "r") as file_object:
    print(type(file_object))

print("File is closed:", file_object.closed)
