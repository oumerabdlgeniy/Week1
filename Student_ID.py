# TASK 2 — Student ID Card

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")
department = input("Enter department: ")
year = int(input("Enter year: "))
university = input("Enter university: ")
phone = input("Enter phone number: ")

print("\n+--------------------------------+")
print("|       STUDENT ID CARD         |")
print("+--------------------------------+")
print(f"| Name: {student_name:<25} |")
print(f"| ID: {student_id:<27} |")
print(f"| Department: {department:<19} |")
print(f"| Year: {year:<25} |")
print(f"| University: {university:<19} |")
print(f"| Phone: {phone:<24} |")
print("+--------------------------------+")