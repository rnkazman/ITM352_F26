# Read a file of names one line at a time and print each name

with open("names.txt", "r") as file_object:
    while (line := file_object.readline()):
        print(line.strip())
        