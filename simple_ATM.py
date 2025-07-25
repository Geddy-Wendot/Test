correct_password = "securepassword123"
correct_username = "admin"

correct_username=input("Enter your username: ")
correct_password=input("Enter your password: ")

if correct_username == "admin" and correct_password == "securepassword123":
    print("Login successful!")
    service =input("Enter the service you want to access: ")
    if service == "ATM":
        print("Accessing ATM service...")
    elif service == "balance":
        print("Accessing balance service...")
    elif service == "transfer":
        print("Accessing transfer service...")
    else:
        print("Invalid service selected.")
            
    


elif correct_username != "admin":
    print("Login failed! Incorrect username.")
elif correct_password != "securepassword123":
    print("Login failed! Incorrect password.")
else:
    print("Login failed! Incorrect username or password.")

