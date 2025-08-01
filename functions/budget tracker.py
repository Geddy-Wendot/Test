def add_entries(entry_type):
    
 data = {}
 print(f"enter your {entry_type} data (enter 'done' when finished): ")


 while True:
   name= input(f"Enter {entry_type.capitalize()} name: ")
   if name.lower() == 'done':
        break

 amount = input(f"Enter {entry_type.capitalize()} amount: ")
 
   