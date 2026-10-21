# Read a CSV file containing window cleaning employee data and compute salary statistics.

import csv
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
