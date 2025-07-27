while True:
    print("Welcome to the Simple Calculator!")
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

    operation = input("Enter operation (+, -, *, /) (or type 'exit' to quit): ")
    if operation.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break
    
    num_1 = float(num_1)
    num_2 = float(num_2)

    
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
            continue
    else:
        result = "Error: Invalid operation."
        continue
    print(f"The result of {num_1} {operation} {num_2} is: {result}")  
    print()
    