correct_password = "securepassword123"
attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Login successful!")
        
        
    else:
        print("wrong password, try again.")

        attempt += 1
        
        
if attempt > max_attempts:
    print("Maximum attempts reached. Access denied.")
        