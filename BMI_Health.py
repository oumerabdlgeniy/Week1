# TASK 10 — BMI Health Information

name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("\n================================")
print("           BMI REPORT")
print("================================")

print(f"\nName: {name}")
print(f"Weight: {weight} kg")
print(f"Height: {height:.2f} m")

print(f"\nBMI: {bmi:.2f}")

print("================================")