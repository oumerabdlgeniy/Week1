# TASK 5 — Ethiopian Shopping Receipt

customer_name = input("Enter customer name: ")

product1 = input("Enter first product: ")
price1 = float(input("Enter first product price: "))
quantity1 = int(input("Enter first product quantity: "))

product2 = input("Enter second product: ")
price2 = float(input("Enter second product price: "))
quantity2 = int(input("Enter second product quantity: "))

total1 = price1 * quantity1
total2 = price2 * quantity2
total = total1 + total2

print("\n========================================")
print("              RECEIPT")
print("========================================")

print(f"\nCustomer: {customer_name}")

print("\nProduct        Price        Qty")
print("----------------------------------------")
print(f"{product1:<15} {price1:<10.2f} {quantity1}")
print(f"{product2:<15} {price2:<10.2f} {quantity2}")

print("----------------------------------------")
print(f"Total:          {total:.2f} ETB")

print("\nThank you for shopping!")
print("========================================")