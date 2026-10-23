# Create a list of tuples that are percentiles of
# household income, with the number of households at each level.
# Calculate the total income of each percentile group and report it.
# Note that, because we are using numpy, we can do this without using a for loop.
import numpy as np

# (percentile, household income, number of households)
hh_income  = [
    (10, 14629, 12500000),
    (20, 25600, 12800000),
    (30, 37002, 12300000),
    (40, 50000, 12900000),
    (50, 63179, 12600000),
    (60, 79542, 12700000),
    (70, 100162, 12400000),
    (80, 130000, 12600000),
    (90, 184292, 12500000),
]

hh_income_array = np.array(hh_income, dtype=np.int64)

# Report the dimensions of the array, and the number of elements in the array.
print("Dimensions of the array: ", hh_income_array.ndim)
print("Dimentions v2: ", hh_income_array.shape)
print("Number of elements in the array: ", hh_income_array.size)

for i in range(len(hh_income_array)):
    print(i, hh_income_array[i][0], hh_income_array[i][1], hh_income_array[i][2])

# Total income of each percentile group = income * number of households
total_income = hh_income_array[:, 1] * hh_income_array[:, 2]
# Equivalent using a for loop:
# total_income = np.zeros(len(hh_income_array), dtype=np.int64)
# for i in range(len(hh_income_array)):
#     total_income[i] = hh_income_array[i][1] * hh_income_array[i][2]

print("\nTotal income of each percentile group:")
for i in range(len(hh_income_array)):
    print(f"Percentile {hh_income_array[i][0]}: ${total_income[i]:,}")
    