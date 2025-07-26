print("welcome to the improved student score program!")
print("If you want to exit, type 'exit' at any time.")

while True:
    name= input("Enter your name: ")
    if name.lower() == 'exit':
        print("Exiting the program.")
        break

    score = input("Enter your score: ")
    if score.lower() == 'exit':
        print("Exiting the program.")
        break

    if not score.isdigit():
        print("Invalid score. Please enter a numeric value.")
        continue

    score = float(score)

    if score >= 90 and score <= 100:
        print(f"{name}, Grade: A")  
    elif score >= 80 and score < 90:
        print(f"{name}, Grade: B")  
    elif score >= 70 and score < 80:
        print(f"{name}, Grade: C")
    elif score >= 60 and score < 70:
        print(f"{name}, Grade: D")  
    elif score < 60 and score >= 0:
        print(f"{name}, Grade: F, you are discontinued.")
    else:
        print("Please enter a valid score.")

    print("Thank you for using the improved student score program!")
    print("If you want to exit, type 'exit' at any time.")
    
    