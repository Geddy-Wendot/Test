num_1=int(input("Enter first number: "))
num_2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2      
elif operation == "*":
    result = num_1 * num_2      
elif operation == "/":
    if num_2 != 0:
        result = num_1 / num_2
    else:
        result = "Error: Division by zero is not allowed."  
else:
    result = "Error: Invalid operation."

print(f"The result of {num_1} {operation} {num_2} is: {result}")  # Displaying the result