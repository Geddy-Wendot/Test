#predicate funcion to validate grades
def has_passed(grade):
    return grade >=50

#function to calculate average marks
def calculate_average(average):
    if average >= 90 and average <= 100:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    
#function to add student and their marks
def add_student(students):
    name = input("Enter student name: ").strip()
    if name in students:
        print(f"Student {name} already exists.")
        return
    
    subjects = {'math', 'science', 'english'}
    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject.capitalize()} (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    total_marks = sum(marks.values())
    average = total_marks / len(subjects)
    grade = calculate_average(average)
    passed = has_passed(average)

    # Add student to the dictionary
    students[name] = {
        'marks': marks,
        'total_marks': total_marks,
        'average': average,
        'grade': grade
    }

    print(f"Student {name} added successfully with grade {grade}.")

#function to display student report
def display_report(students):
    if not students:
        print("No students to display.")
        return
    
    print("\nStudent Report:")
    for name, data in students.items():
        print(f"name: {name}")

        for subject,score in data['marks'].items():
            print(f"{subject:<8}: {score}")

        print(f"Total Marks: {data['total_marks']}")
        print(f"Average Marks: {data['average']:.2f}")
        print(f"Grade: {data['grade']}")
        print(f"Passed: {'Yes' if has_passed(data['average']) else f"status: {data['status']} NO "}")    
    
    print("----------------------")

# Main function to run the student management system
def main():
    students = {}
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Report")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_report(students)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

main()            
    
    