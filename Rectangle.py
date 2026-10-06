# TASK 3 — Area and Perimeter Calculator

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("\n================================")
print("       RECTANGLE REPORT")
print("================================")

print(f"\nLength: {length} m")
print(f"Width: {width} m")

print(f"\nArea: {area} m²")
print(f"Perimeter: {perimeter} m")

print("================================")