numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#to count even and odd numbers in the list
even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
        print(f"{number} is even")
    else:
        odd_count += 1
        print(f"{number} is odd")

print(f"Total even numbers: {even_count}")
print(f"Total odd numbers: {odd_count}")    