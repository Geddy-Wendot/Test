item=input("enter item: ")
price=float(input("enter price: "))

# Create a dictionary to store the item and its price
record = {
    item: price  # Using the item as the key and price as the value,
}

#add multiple items
new_item = input("do you want to add another item? (yes/no): ")
if new_item.lower() == "yes":
    new_item_name = input("Enter the new item name: ")
    new_item_price = float(input("Enter the new item price: "))
    record[new_item_name] = new_item_price

#remove an item
remove_item = input("do you want to remove an item? (yes/no): ")
if remove_item.lower() == "yes":
    item_to_remove = input("Enter the item to remove: ")
    if item_to_remove in record:
        del record[item_to_remove]
        print(f"Item '{item_to_remove}' removed successfully.")
    else:
        print(f"Item '{item_to_remove}' not found in the record.")

# total price calculation
total_price = sum(record.values()) 
print("Total price of all items:", total_price)  # Displaying the total price

#final record
print(f"Final record of items and prices:")
for item, price in record.items():
    print(f"{item}: ${price:.2f}")  # Displaying each item and its price