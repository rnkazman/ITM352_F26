# Create a Pandas dataframe from individual lists.
# Do some simple stats on the data
import pandas as pd

# Lists of individuals' names, ages, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

raw_data = zip(ages, gender)

# Create a Pandas dataframe from the lists
df = pd.DataFrame(data=raw_data, index=names, columns=["Age", "Gender"])

summary = df.describe()  # Get summary statistics for the dataframe
print(summary)  # Print the summary statistics

# Calculate average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
print("\nAverage age by gender:")
print(average_age_by_gender)
