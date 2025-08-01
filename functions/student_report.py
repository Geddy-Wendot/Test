def student_report(student_name, age, school, grade= "not assigned", *marks, **extras):
    print(f"Student Name: {student_name}")
    print(f"Age: {age}")
    print(f"School: {school}")
    print(f"Grade: {grade}")

    if marks:
        avg_marks = sum(marks) / len(marks)
        print(f"Average Marks: {avg_marks:.2f}")
    else:
        print("No marks provided.")

    if extras:
        print("Additional Information:")
        for key, value in extras.items():
            print(f"{key}: {value}")
    else:
        print("No additional information provided.")

student_report(
    "Alice",
    15,
    "Greenwood High",
    "A",
    85, 90, 78,
    hobby="Chess",
    city="New York"
)

