# Read taxi_1000.csv and calulate the total of all fares, average fare, 
# and max trip distance.
import csv

filename = "..\\taxi_1000.csv"

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)

    total_fare = 0.0
    max_distance = 0.0
    average_fare = 0.0
    num_rows = 0

    for row in csv_reader:
        if num_rows == 0:
            # Skip the header row
            fare_index = row.index('Fare')  # Get the index of the fare column
            distance_index = row.index('Trip Miles')  # Get the index of the distance column
            num_rows += 1
            continue

        if (num_rows > 0):
            fare = float(row[fare_index])
            distance = float(row[distance_index])

            total_fare += fare
            if distance > max_distance:
                max_distance = distance

        num_rows += 1

if num_rows > 1:  # Ensure there are data rows to avoid division by zero
    average_fare = total_fare / (num_rows - 1)  # Subtract 1 for the header row

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Max Trip Distance: {max_distance:.2f} miles")
