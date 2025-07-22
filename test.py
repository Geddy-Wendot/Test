#list and tuple operations in Python
# This script demonstrates basic operations on lists and tuples in Python.

my_list=[1,"apple",3.14,True]
print(my_list)
print(type(my_list))
print(my_list[0])  # Accessing the first element
print("First 2 elements:", my_list[:2])  # Slicing to get the first two elements
print("last 2 elements:", my_list[-2:])  # Slicing to get the last two elements
print("Length of the list:", len(my_list))  # Getting the length of the list
print("Is 'apple' in the list?", "apple" in my_list)  # Checking for membership

my_list.remove("apple")  # Removing an element
print("List after removing 'apple':", my_list)  # Displaying the list after removal

my_list.append("banana")  # Adding an element
print("List after appending 'banana':",my_list)  # Displaying the list after appending

del my_list[1]  # Deleting the second element
print("List after deleting the second element:", my_list)  # Displaying the list after deletion

print(my_list)

my_tuple = (1, "apple", 3.14, True)
print(my_tuple)

print(my_tuple[0])  # Accessing the first element of the tuple
print("First 2 elements of the tuple:", my_tuple[:2])  # Slicing to get the first two elements of the tuple
print("Length of the tuple:", len(my_tuple))  # Getting the length of the tuple 
print("Is 'apple' in the tuple?", "apple" in my_tuple)  # Checking for membership in the tuple
print("Tuple after operations (unchanged):", my_tuple)  # Tuples are immutable, so it remains unchanged

list_to_tuple = tuple([1, 2, 3, 4])  # Converting a list to a tuple
print("Converted list to tuple:", list_to_tuple)  # Displaying the converted tuple

tuple_to_list = list((1,2,3,4))  # Converting a tuple to a list
print("Converted tuple to list:", tuple_to_list)  # Displaying the converted list

#sets in Python
numbers = [1,2,2,3,4,5,5,6]
unique_numbers = set(numbers)  # Creating a set from a list to remove duplicates

unique_numbers.add(7)  # Adding an element to the set

unique_numbers.remove(2)  # Removing an element from the set

print(unique_numbers)  # Displaying the set after operations

#dictionary operations in Python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict["weight"]=30
print(my_dict)  # Displaying the dictionary after adding a new key-value pair

del my_dict["city"]  # Deleting a key-value pair from the dictionary
print(my_dict)  # Displaying the dictionary after deletion


#creating a dictionary
student_info = {
    "name": "John Doe",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}

#add a new key-value pair
student_info["graduated"] = False 

#change age
student_info["age"] = 21

#remove a key-value pair
del student_info["courses"]

#loop through the dictionary
for key, value in student_info.items():
    print(key, ":", value)


#convertion
a="15"
b="35"

a = int(a)  # Convert string to integer
b = int(b)  # Convert string to integer

c= a + b  # Perform addition
print(f"the sum of {a} and {b} is {c}")  # Display the result