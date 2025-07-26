student = []
add_names = set()

while True:
   print("Welcome to the Student Management System!")
   print("1. Add Student")
   print("2. View Students")
   print("3. Search Student")
   print("4. remove Student")
   print("5. Exit")

   choice = input("Please enter your choice (1-5): ")

   if choice == '1':
      name = input("Enter student's name: ")
      if name in add_names:
            print(f"{name} is already in the system.")
            continue
      
      age = input("Enter student's age: ")
      if not age.isdigit():
        print("Invalid age. Please enter a numeric value.")
        continue
   
      course = input("Enter student's course: ")
      student.append({'name': name, 'age': int(age), 'course': course})
      add_names.add(name)
      print(f"Student {name} added successfully!")

   elif choice == '2':
    if not student:
        print("No students found.")
        continue
    print("List of Students:")
    for i, s in enumerate(student, start=1):
        print(f"{i}. Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    
   elif choice == '3':
        search_name = input("Enter the name of the student to search: ")
        found = False
        for s in student:
            if s['name'].lower() == search_name.lower():
                print(f"Student found: Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
                found = True
                break
        if not found:
            print(f"No student found with the name {search_name}.")

   elif choice == '4':
       remove_name = input("Enter the name of the student to remove: ")
       for s in student:
           if s['name'].lower() == remove_name.lower():
               student.remove(s)
               add_names.remove(remove_name)
               print(f"Student {remove_name} removed successfully!")
               break
       else:
        print(f"No student found with the name {remove_name}.")
 
   elif choice == '5':
        print("Exiting the Student Management System. Goodbye!")
        break
   
   else:
        print("Invalid choice. Please enter a number between 1 and 5.")
           
