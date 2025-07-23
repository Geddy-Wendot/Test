name=input("Enter your name: ")
age=int(input("Enter your age: "))
courses=input("Enter your courses (comma separated): ")

courses_list = courses.split(",")  # Convert comma-separated string to list
courses_set = set(course.strip() for course in courses_list)  # Convert list to set to remove duplicates

student = {
    "name": name,
    "age":int(age),
    "courses": list(courses_set)  # Store courses as a list
}

print("student info created successfully!")
print(f"Name:{student['name']}")
print(f"Age:{student['age']}")
print(f"Courses:{student['courses']}")

#update age
update_age = input("do you want to update age? (yes/no): ")
if update_age.lower() == "yes":
    new_age = int(input("Enter new age: "))
    student["age"] = new_age

#option to remove a course
remove_course = input("do you want to remove a course? (yes/no): ")
if remove_course.lower() == "yes": 
    course_to_remove = input("Enter the course to remove: ")
    if course_to_remove in student["courses"]:
        student["courses"].remove(course_to_remove)
        print(f"Course '{course_to_remove}' removed successfully.")
    else:
        print(f"Course '{course_to_remove}' not found in the list.")

#print final student info
print("Final student info:")
print(student)        