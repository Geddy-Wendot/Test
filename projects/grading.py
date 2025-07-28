student= {}

while True:
    print("\nStudent Grading System")
    print ("1. Add Student and grade")
    print ("2. View Students and grades")
    print ("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
       num = input("Enter number of students to add: ")
       if not num.isdigit() or int(num) <= 0:
            print("Invalid number. Please enter a positive integer.")
            continue
        
       num = int(num)
       for i in range(num):
            name = input(f"Enter name of student {i+1}: ")
            if name in student:
                print(f"Student {name} already exists. Please enter a different name.")
                continue

            marks = input(f"Enter marks for {name}: ")
            if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
                print("Invalid marks. Please enter a number between 0 and 100.")
                continue
            marks = int(marks)
            student[name] = marks
    elif choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\nList of Students and Grades:")
            for name, marks in student.items():
                
                if marks >= 90:
                    grade = 'A'
                elif marks >= 80:
                    grade = 'B'
                elif marks >= 70:
                    grade = 'C'
                elif marks >= 60:
                    grade = 'D'
                else:
                    grade = 'F'
                
                print(f"Student: {name}, Marks: {marks}, Grade: {grade}")

    elif choice == '3':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
             
            
