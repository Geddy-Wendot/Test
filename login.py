correct_password = "securepassword123"
correct_username = "admin"

name=input("Enter your username: ")
password=input("Enter your password: ")

if name == correct_username and password == correct_password:
    print("Login successful!")
elif name != correct_username:
    print("Login failed! Incorrect username.")
elif password != correct_password:
    print("Login failed! Incorrect password.")    
else:
    print("Login failed! Incorrect username or password.")  