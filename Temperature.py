# TASK 4 — Temperature Station

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("\n================================")
print("       TEMPERATURE REPORT")
print("================================")

print(f"\nCelsius: {celsius}°C")
print(f"Fahrenheit: {fahrenheit}°F")

fahrenheit_input = float(input("\nEnter temperature in Fahrenheit: "))

celsius_converted = (fahrenheit_input - 32) * 5 / 9

print(f"Celsius conversion: {celsius_converted:.2f}°C")

print("================================")