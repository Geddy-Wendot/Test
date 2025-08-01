def student_report(name, school = "unknown school", *marks, **details):

    if not marks:
        print(f"No marks provided for {name}.")
        return

    average_marks = sum(marks) / len(marks)

    if average_marks >=90 and average_marks <= 100:
        grade = "A"
    elif average_marks >= 80:
        grade = "B"
    elif average_marks >= 70:
        grade = "C"
    elif average_marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student Name: {name}")
    print(f"School: {school}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")

    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")
student_report(
    "Bob",
    "Riverdale High",
    88, 92, 79,
    age=16,
    city="Los Angeles"
)