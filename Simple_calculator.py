print("Simple Calculator")
print("Enter two numbers to perform operations.")
try:
    num1 = float(input("Enter the first number: "))
    operationSelected = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Please select a number.")
else:
    if operationSelected == "+":
        print(f"Sum: {num1 + num2}")
    elif operationSelected == "-":
        print(f"Difference: {num1 - num2}")
    elif operationSelected == "*":
        print(f"Product: {num1 * num2}")
    elif operationSelected == "/":
        print(f"Quotient: {num1 / num2}")
    else:
        print("Invalid operation selected. Please choose from +, -, *, or /.")