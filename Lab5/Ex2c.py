
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

trips = dict(zip(trip_durations, trip_fares))
print(trips)

trip_num = int(input("What trip do you want?"))

print("The duration of the trip is:", trip_durations[trip_num-1], " miles")
print("The fare of the trip is:", trip_fares[trip_num-1])
