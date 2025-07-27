item = input("Enter item: ")
cost = float(input("Enter cost: "))

# Create a dictionary to store the item and its cost
record = {
    item: cost }

new_item = input("Do you want to add another item? (yes/no): ")
if new_item.lower() == "yes":
    new_item_name = input("Enter the new item name: ")
    new_item_cost = float(input("Enter the new item cost: "))
    record[new_item_name] = new_item_cost

# Remove an item
remove_item = input("Do you want to remove an item? (yes/no): ")    
if remove_item.lower() == "yes":
    item_to_remove = input("Enter the item to remove: ")
    if item_to_remove in record:
        del record[item_to_remove]
        print(f"Item '{item_to_remove}' removed successfully.")
    else:
        print(f"Item '{item_to_remove}' not found in the record.")

# Total cost calculation
total_cost = sum(record.values())
print("Total cost of all items:", total_cost)  # Displaying the total cost

print(f"Final record of items and costs: {record}")    