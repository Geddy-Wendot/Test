def add (x,y):
    return x + y
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x * y
def divide (x,y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'exit':"Exiting the calculator. Goodbye!"
}

while True:
    print("Welcome to the Customizable Calculator!")
    print()
    print("You can perform addition, subtraction, multiplication, and division.")

    num_1 = input("Enter first number (or type 'exit' to quit): ")
    if num_1.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    num_2 = input("Enter second number (or type 'exit' to quit): ")
    if num_2.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    op = input("Enter operation (+, -, *, /) (or type 'exit' to quit): ")
    if op.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break



    num_1 = float(num_1)
    num_2 = float(num_2)

    if op in operation:
     result = operation[op](num_1, num_2)
    print(f"The result of {num_1} {op} {num_2} is: {result}")

print()

    
  
