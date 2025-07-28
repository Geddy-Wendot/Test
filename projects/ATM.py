pin = 444888
username = "user123"

pin = int(input("Enter your PIN: "))
username = input("Enter your username: ")

if pin == 444888 and username == "user123":
    print("Login successful!")
    service = input("Enter the service you want to access (ATM, balance, transfer): ")
    if service.lower() == "atm":
        print("Accessing ATM service...")
    elif service.lower() == "balance":
        print("Accessing balance service...")
    elif service.lower() == "transfer":
        print("Accessing transfer service...")
    else:
        print("Invalid service selected.")

else:
    if pin != 444888:
        print("Login failed! Incorrect PIN.")
    if username != "user123":
        print("Login failed! Incorrect username.")
    if pin != 444888 and username != "user123":
        print("Login failed! Incorrect PIN and username.")

    else:
        print("Login failed! Please try again.")
