# TASK 7 — Travel Planner

destination = input("Enter destination: ")
distance = float(input("Enter distance in kilometers: "))
speed = float(input("Enter average speed in km/h: "))

travel_time = distance / speed

hours = int(travel_time)
minutes = int((travel_time - hours) * 60)

print("\n========================================")
print("           TRAVEL INFORMATION")
print("========================================")

print(f"\nDestination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h")

print(f"\nEstimated Travel Time: {hours} hours {minutes} minutes")

print("========================================")