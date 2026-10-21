# Read a CSV file containing window cleaning employee data and compute salary statistics.
# print info about file existence and permissions before reading the file

import csv
import os

# Check if the file exists and is readable
if not os.path.exists("window_cleaning_employees.csv"):
    print(f"Error: File window_cleaning_employees.csv not found.")
    exit(1)

if not os.access("window_cleaning_employees.csv", os.R_OK):
    print("Error: File is not readable.")
    exit(1)
else:
    file_size = os.path.getsize("window_cleaning_employees.csv")
    print(f"File exists and is readable. Size: {file_size} bytes.")


csv_filename = "window_cleaning_employees.csv"
salaries = []

# Read the CSV file and store the salaries in a list
with open(csv_filename, mode='r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Skip the header row
    print(f"Headers: {headers}")  # Print the headers for debugging
    salary_index = headers.index("Annual_Salary")  # Find the index of the Salary column
    for row in reader:
        salary = float(row[salary_index])  # Convert salary to float
        salaries.append(salary)

    # Compute salary stats
    avg_salary = sum(salaries) / len(salaries)
    min_salary = min(salaries)
    max_salary = max(salaries)

    # Print the salary stats
    print(f"Average Salary: ${avg_salary:.2f}")
    print(f"Minimum Salary: ${min_salary:.2f}")
    print(f"Maximum Salary: ${max_salary:.2f}")
