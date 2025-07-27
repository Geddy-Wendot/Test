start_number = int(input("Enter the starting number for the multiplication table: "))
end_number = int(input("Enter the ending number for the multiplication table: "))

print("Multiplication Table from", start_number, "to", end_number)
for i in range(start_number, end_number + 1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j} ") 
       
    print()  # Print a newline for better readability between tables
